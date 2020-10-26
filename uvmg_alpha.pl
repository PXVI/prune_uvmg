#  -----------------------------------------------------------------------------------
#  Module Name  : uvmg_alpha
#  Date Created : 18:44:10 IST, 25 October, 2020 [ Sunday ]
# 
#  Author       : pxvi
#  Description  : The main script for perl based UVM tb generation
#  -----------------------------------------------------------------------------------
# 
#  MIT License
# 
#  Copyright (c) 2020 k-sva
# 
#  Permission is hereby granted, free of charge, to any person obtaining a copy
#  of this software and associated documentation files (the Software), to deal
#  in the Software without restriction, including without limitation the rights
#  to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#  copies of the Software, and to permit persons to whom the Software is
#  furnished to do so, subject to the following conditions:
# 
#  The above copyright notice and this permission notice shall be included in all
#  copies or substantial portions of the Software.
# 
#  THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#  OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#  SOFTWARE.
# 
#  ----------------------------------------------------------------------------------- */

#!/usr/bin/perl

=begin comment
This is the first phase of the UVM tb generation automation script. This will essentially
automate most of the grunt work of creating and crafting a TB which is corrected connected
and compiler clean. A more advance version of this will also manage the TB on the fly, but
for now this script will just generate a UVM testbench which will be ready to get coded
directly after generation.
=cut

$displayHelp = 0;

#print "$#ARGV\n";

if( ( ( $#ARGV + 1 ) > 0 ) ){
    if( ( $#ARGV + 1 ) != 2 ){
        $displayHelp = 1;
    }
    foreach $o ( @ARGV ){
        if( ( $o eq "-h" ) or ( $o eq "--help" ) ){
            $displayHelp = 1;
        }
    }

    if( $displayHelp != 1 ){

        $testbench_name = "$ARGV[0]";
        $allFilesInPath = "./*";
        $tbBasePath = "./$testbench_name/";
        
        # Delete everything in the current directory first
        # Not Needed Anymore. Will Add it again during testing # 
        system ( "rm -rf ./*" );
        
        mkdir ( $testbench_name ) or die( "Could't make the directoy" );
        
        open( FH, '<', $ARGV[1] ) or die( "Failed to open the file provided as an argument" );
        
        @dirTags = ( "dir" );
        %uvmCompTags = (    "uvm_env" => 0, 
                            "uvm_agent" => 1, 
                            "uvm_driver" => 1, 
                            "uvm_sequencer" => 1, 
                            "uvm_monitor" => 1, 
                            "uvm_subscriber" => 1, 
                            "uvm_test" => 1, 
                            "uvm_component" => 1, 
                            "uvm_scoreboard" => 1, 
                            "uvm_random_stimulus" => 1
                    );
        %uvmObjTags = (     "uvm_void" => 0, 
                            "uvm_object" => 1, 
                            "uvm_report_object" => 2, 
                            "uvm_transaction" => 5, 
                            "uvm_sequence_item" => 5, 
                            "uvm_sequence_base" => 5
                    );
        
        %fileTagsExt = ( "svfile" => "sv", "hfile" => "h", "vfile" => "v", "listfile" => "list", "shfile" => "sh", "plfile" => "pl", "pyfile" => "py" );
        
        $startLoc = "./$testbench_name";
        $currLoc = "$startLoc";
        
        $heirarchyCreationDone = 0;
        
        $dirBegins = 0;
        $fileBegins = 0;
        $dirEnds = 0;
        $fileEnds = 0;
        
        $uvmFilePath = ""; # Holds the path to the last UVM file that the script is inside of
        $workingFilePath = "";
        $workingFileExt = "";
        
        # -------------------------
        # Heirarchy Creation Script
        # -------------------------
        
        while( <FH> ){
            #print $_;
            $line = $_;
            $line =~ s/[ ]*//g;
            #print $line;
        
            @spl = split( ':', $line );
            $arrSize = $#spl;
            #print "$arrSize\n";
        
        
            $tempInt = 0;
            #foreach $i ( @spl ){
            #    if( $tempInt < $arrSize ){
            #        print "$i\n";
            #    } else {
            #        print "$i";
            #    }
            #    runFileTagsCheck( $i );
            #    $tempInt = $tempInt + 1;
            #}
            $sizeArr = $#spl;
            $spl[$sizeArr] =~ s/\n//g;
        
            if( $sizeArr != -1 ){
                runFileTagsCheck( @spl );
            }
        }
        
        $heirarchyCreationDone = 1;
        close( FH );

        # ---------------------------------
        # Code Creation Script
        # ---------------------------------

        open( FH, '<', $ARGV[1] ) or die( "Failed to re-open the file for code addtion" );

        while( <FH> ){
            #print $_;
            $line = $_;
            $line =~ s/[ ]*//g;
            #print $line;
        
            @spl = split( ':', $line );
            $arrSize = $#spl;
        
            $tempInt = 0;

            $sizeArr = $#spl;
            $spl[$sizeArr] =~ s/\n//g;
        
            if( $sizeArr != -1 ){
                runFileTagsCheck( @spl );
            }
        }
        
        close( FH );
    }
}else{
 $displayHelp = 1;
}

if( $displayHelp == 1 ){
    print "# ---------------------------------------------------------------\n";
    print "# UVMG Alpha Build v0.1 : Help Section\n";
    print "# ---------------------------------------------------------------\n";
    print "# This is a pre build automation script which is used to generate\n";
    print "# a simple UVM testbench with configurable architecture depending\n";
    print "# on the needs of the designer. One can create quick testbenches \n";
    print "# with this and have no hassel of getting the compilation right  \n";
    print "# or making uneccessary connections throughout the tb.           \n";
    print "# All you require is a simple .fmt file with the architecture    \n";
    print "# laid out and everything will be generated on the fly completely\n";
    print "# ready for simulation. Although, note that you will still have  \n";
    print "# to code the functional parts of the testbench on your own.     \n";
    print "# Thanks for trying this out :D                                  \n";
    print "# \n";
    print "# -h , --help : Gives the full help guide\n";
    print "# This perl script takes two inputs :\n"; 
    print "# 1. Top TB Name\n";
    print "# 2. <.fmt> file\n";
    print "# ---------------------------------------------------------------\n";
}

# -----------
# Subroutines
# -----------

sub runFileTagsCheck{
    $argsNum = $#_ + 1;
 
    #print "Before -> dB : $dirBegins, dE : $dirEnds, fB : $fileBegins, fE : $fileEnds\n";

    if( ( $argsNum > 2 ) and ( $_[0] eq "begin" ) and ( $_[2] eq "dir" ) ){ # Directory Creation
        if( $heirarchyCreationDone == 1 ){
            moveIn( $_[1] );
        }else{
            createMoveIn( $_[1] );
        }
        #print "1 ------------ > $_[0] : $_[1] : $_[2]\n";
        $dirBegins = $dirBegins + 1;
    }elsif( ( $argsNum > 2 ) and ( $_[0] eq "begin" ) ){ # For non directory files
        #print "2 ------------ > $_[0] : $_[1] : $_[2]\n";
        $fileBegins = $fileBegins + 1;
        if( $heirarchyCreationDone == 1 ){
            if( exists( $fileTagsExt{$_[2]} ) ){
                $workingFilePath = "$currLoc/$_[1].$fileTagsExt{$_[2]}";
                $workingFileExt = "$fileTagsExt{$_[2]}";
            }else{
                addUVMCode( @_ ); # Eg; begin:class_name:classtype
            }
        }else{
            createFile( @_ );
        }
    }elsif( $argsNum == 1 and "$_[0]" == "end" ){
        #print "3 ------------ > $_[0] : $_[1] : $_[2]\n";

        if( $fileBegins == $fileEnds ){
            moveOut();
            $fileBegins = 0;
            $fileEnds = 0;
            $dirEnds = $dirEnds + 1;
        }else{
            $fileEnds = $fileEnds + 1;
        }
    }else{
        print "[E] The arguments count never be less than 3 other than for end keyword : $argsNum\n"
    }
    #print "After  -> dB : $dirBegins, dE : $dirEnds, fB : $fileBegins, fE : $fileEnds\n";
}

sub createMoveIn{ # This is used to create & update the current heirarchy path where the script is : Path moves one dir down

    foreach $m ( @_ ){
        $currLoc = "$currLoc/$m";
        mkdir ( $currLoc ) or die( "Failed to create the directory $currLoc" );
        #print "Move In  : $currLoc\n";
    }
}

sub moveIn{ # This is used to update the current heirarchy path where the script is : Path moves one dir down

    foreach $m ( @_ ){
        $currLoc = "$currLoc/$m";
        #print "Move In  : $currLoc\n";
    }
}

sub moveOut{ # This is used to update the current heirarchy path where the script is : Path moves one dir up
    @spl = split( '/', $currLoc );
    $arrSize = $#spl;

    $tempLoc = ".";
    $len = 0;

    foreach $k ( @spl ){
        if( ( $len != 0 ) and ( $len < $arrSize ) ){
            $tempLoc = "$tempLoc/$k";
        }

        $len = $len + 1;
    }

    $currLoc = $tempLoc;
    #print "Move Out : $currLoc\n";
}

sub createFile{ # This used to create a new file for the first time
    if( ( $#_ + 1 ) > 2 ){
        if( exists( $fileTagsExt{$_[2]} ) ){ # Check is the extention is suported or not
            system( "touch $currLoc/$_[1].$fileTagsExt{$_[2]}" );
            print "File created : $currLoc/$_[1].$fileTagsExt{$_[2]}\n";

            @newArr = ( "$fileTagsExt{$_[2]}", "$currLoc/$_[1].$fileTagsExt{$_[2]}" );

            # Comment this out if you don't want my lic to be generated. Otherwise, just replace k-sva with your name and you'll have nice MIT lic in you newly generated code.
            insertLic( @newArr );
        }else{
            #print "[E] File extension is not supported : $_[2]\n"
        }
    }else{
        print "[E] Error in the syntax\n"
    }
}

sub insertLic(){
    open( NH, ">>", "$_[1]" ) or die( "[E] Failed to open the file for appending" ); # Open the file in append mode

    if( ( $_[0] eq "sv" ) or ( $_[0] eq "v" ) ){
        $fcomment = "/*";
        $comment = " *";
        $ecomment = "*/";
    }else{
        $fcomment = "#";
        $comment = "# ";
        $ecomment = "";
    }

    %monArr = ( 0 => "January", 1 => "Febuary", 2 => "March", 3 => "April", 4 => "May", 5 => "June", 6 => "July", 7 => "August", 8 => "September", 9 => "October", 10 => "November", 11 => "December" );
    %wdayArr = ( 0 => "Sunday", 1 => "Monday", 2 => "Tuesday", 3 => "Wednesday", 4 => "Thursday", 5 => "Friday", 6 => "Saturday" );

    my ($sec,$min,$hour,$mday,$mon,$year,$wday,$yday,$isdst) = localtime(time);
    $year += 1900;
    #print "$mon : $wday\n";
    $mon = $monArr{$mon};
    $wday = $wdayArr{$wday};
    if( $min < 10 ){
        $min = "0$min";
    }
    if( $sec < 10 ){
        $sec = "0$sec";
    }
    if( $hour < 10 ){
        $hour = "0$hour";
    }

    print NH "$fcomment -----------------------------------------------------------------------------------\n";
    print NH "$comment Module Name  : \n";
    print NH "$comment Date Created : $hour:$min:$sec IST, $mday $mon, $year [ $wday ]\n";
    print NH "$comment \n";
    print NH "$comment Author       : pxvi\n";
    print NH "$comment Description  : \n";
    print NH "$comment -----------------------------------------------------------------------------------\n";
    print NH "$comment \n";
    print NH "$comment MIT License\n";
    print NH "$comment \n";
    print NH "$comment Copyright (c) $year k-sva\n";
    print NH "$comment \n";
    print NH "$comment Permission is hereby granted, free of charge, to any person obtaining a copy\n";
    print NH "$comment of this software and associated documentation files (the Software), to deal\n";
    print NH "$comment in the Software without restriction, including without limitation the rights\n";
    print NH "$comment to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n";
    print NH "$comment copies of the Software, and to permit persons to whom the Software is\n";
    print NH "$comment furnished to do so, subject to the following conditions:\n";
    print NH "$comment \n";
    print NH "$comment The above copyright notice and this permission notice shall be included in all\n";
    print NH "$comment copies or substantial portions of the Software.\n";
    print NH "$comment \n";
    print NH "$comment THE SOFTWARE IS PROVIDED AS IS, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n";
    print NH "$comment IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n";
    print NH "$comment FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n";
    print NH "$comment AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n";
    print NH "$comment LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n";
    print NH "$comment OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n";
    print NH "$comment SOFTWARE.\n";
    print NH "$comment \n";
    print NH "$comment ----------------------------------------------------------------------------------- $ecomment\n";

}

sub addUVMCode{
    if( exists( $uvmCompTags{$_[2]} ) or exists( $uvmObjTags{$_[2]} )  ){
        print "UVM Tag exists : $_[2] ( $workingFilePath : $workingFileExt )\n";

        # Add the generic UVM class code to the open file
        open( NH, ">>", "$workingFilePath" ) or die( "[E] Failed to open the file for appending" ); # Open the file in append mode

        $newFunc = "
    function new( string name = \"$_[1]\", uvm_component parent = null );
        // --------------------------
        // New Constructot - Top Down
        // --------------------------
        super.new( name, parent );

    endfunction
";
        $buildPhase = "
    virtual function void build_phase( uvm_phase phase );
        // ---------------------------
        // Build Phase Code - Top Down
        // ---------------------------
        super.build_phase( phase );

    endfunction
";
        $connectPhase = "
    virtual function void connect_phase( uvm_phase phase );
        // ------------------------------
        // Connect Phase Code - Bottom Up
        // ------------------------------
        super.connect_phase( phase );

    endfunction
";
        $eoePhase = "
    virtual function void end_of_elaboration_phase( uvm_phase phase );
        // -----------------------------------------
        // End Of Elaboration Phase Code - Bottom Up
        // -----------------------------------------
        super.end_of_elaboration( phase );

    endfunction
";
        $sosPhase = "
    virtual function void start_of_simulation_phase( uvm_phase phase );
        // ------------------------------------------
        // Start Of Simualtion Phase Code - Bottom Up
        // ------------------------------------------
        super.start_of_simulation_phase( phase );

    endfunction
";
    if( $_[2] == "uvm_test" ){
        $mainPhase = "
    task main_phase( uvm_phase phase );
        // -------------------------------
        // Test Main Phase Code - Parallel
        // -------------------------------
        phase.raise_objection( this );

        super.main_phase( phase );
       
        // Time Consuming Code Here

        phase.drop_objection( this );

    endfunction
";
    }else{
        $mainPhase = "
    task main_phase( uvm_phase phase );
        // --------------------------
        // Main Phase Code - Parallel
        // --------------------------
        super.main_phase( phase );

    endfunction
";
    }
        $extractPhase = "
    virtual function void extract_phase( uvm_phase phase );
        // ------------------------------
        // Extract Phase Code - Bottom Up
        // ------------------------------
        super.extract_phase( phase );

    endfunction
";
        $checkPhase = "
    virtual function void check_phase( uvm_phase phase );
        // ----------------------------
        // Check Phase Code - Bottom Up
        // ----------------------------
        super.check_phase( phase );

    endfunction
";
        $reportPhase = "
    virtual function void report_phase( uvm_phase phase );
        // -----------------------------
        // Report Phase Code - Bottom Up
        // -----------------------------
        super.report_phase( phase );

    endfunction
";
        $finalPhase = "
    virtual function void final_phase( uvm_phase phase );
        // ---------------------------
        // Final Phase Code - Top Down
        // ---------------------------
        super.final_phase( phase );

    endfunction
";
        $preBody = "
    virtual task pre_body();
        // -------------
        // Pre Body Code
        // -------------
        super.pre_body();

    endfunction
";
        $body = "
    virtual task body();
        // ---------
        // Body Code
        // ---------
        super.body();

    endfunction
";
        $postBody = "
    virtual task post_body();
        // --------------
        // Post Body Code
        // --------------
        super.post_body();

    endfunction
";

        # The Complete Code put togather

        if( 
            exists( $uvmObjTags{$_[2]} )
            ){
                
                # Add the new object/obj child to the obj hash list
                $uvmObjTags{$_[1]} = 0; # Default value

                $codeVarStart = "
class $_[1] extends $_[2];

    `uvm_object_utils( $_[1] )
                   ";
                $buildPhase = "";
                $connectPhase = "";
                $eoePhase = "";
                $sosPhase = "";
                $mainPhase = "";
                $extractPhase = "";
                $checkPhase = "";
                $reportPhase = "";
                $finalPhase = "";

                if( $uvmObjTags{$_[2]} != 5 ){
                    $preBody = "";
                    $body = "";
                    $postBody = "";
                }else{
                    $uvmObjTags{$_[1]} = 5; # Derivative of uvm_sequence_item
                }

            }elsif( exists( $uvmCompTags{$_[2]} ) ){
                
                # Add the new component/component child to the component hash list
                $uvmCompTags{$_[1]} = 0; # Default value

                $codeVarStart = "
class $_[1] extends $_[2];

    `uvm_component_utils( $_[1] )
                ";
            }
        $codeVarEnd = "
endclass
                   ";

        print NH "$codeVarStart";
        print NH "$newFunc";

        print NH $preBody;
        print NH $body;
        print NH $postBody;

        print NH "$buildPhase";
        print NH "$connectPhase";
        print NH "$eoePhase";
        print NH "$sosPhase";
        print NH "$mainPhase";
        print NH "$extractPhase";
        print NH "$checkPhase";
        print NH "$reportPhase";
        print NH "$finalPhase";
        
        print NH "$codeVarEnd";

    }else{
        print "UVM Tag Does not exist : $_[2] ( $workingFilePath : $workingFileExt )\n";
    }
}
