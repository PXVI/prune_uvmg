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
        # system ( "rm -rf ./*" );
        
        mkdir ( $testbench_name ) or die( "Could't make the directoy" );
        
        open( FH, '<', $ARGV[1] ) or die( "Failed to open the file provided as an argument" );
        
        @dirTags = ( "dir" );
        @uvmTags = ( "uvm_env", "uvm_agent", "uvm_driver", "uvm_sequencer", "uvm_monitor", "uvm_subscriber", "uvm_test", "uvm_sequence" );
        
        %fileTagsExt = ( "svfile" => "sv", "hfile" => "h" );
        
        $startLoc = "./$testbench_name";
        $currLoc = "$startLoc";
        
        $heirarchyCreationDone = 0;
        
        $dirBegins = 0;
        $fileBegins = 0;
        $dirEnds = 0;
        $fileEnds = 0;
        
        $uvmFilePath = ""; # Holds the path to the last UVM file that the script is inside of
        
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
        createMoveIn( $_[1] );
        #print "1 ------------ > $_[0] : $_[1] : $_[2]\n";
        $dirBegins = $dirBegins + 1;
    }elsif( ( $argsNum > 2 ) and ( $_[0] eq "begin" ) ){ # For non directory files
        #print "2 ------------ > $_[0] : $_[1] : $_[2]\n";
        $fileBegins = $fileBegins + 1;
        createFile( @_ );
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
        }else{
            print "[E] File extension is not supported : $_[2]\n"
        }
    }else{
        print "[E] Error in the syntax\n"
    }
}
