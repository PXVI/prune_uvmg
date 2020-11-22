# uvmg_alpha
Automated custom configurable UVM Test Environment generation tool ( terminal &amp; gui supported )<br /><br />

### Updates

#### Perl Script ( Used for the tb generation )
<br />

  - The basic perl script has been added
  - The script accepts 2 arguments ( top tb directory name & layout.fmt file )
  - The script generates the file and directory heirarchy with proper detail
  - The LISCENSE is added for the generated files
  - Basic UVM component/object code additions happen in the generated files
  - Script automatically maintains uvm_object and uvm_component lists and updates for any new children of these base classes
  - Only constraint for the current model is that the script is linear and follows a streamlined heirarchy
  - **Pending :** Verilog/SystemVerilog interface static block code generation
  - **Pending :** Testbench top file generation
  - **Pending :** TLM1 ports implementation and connections generation
  - **Pending :** Comments updation implementation

<br />

#### Python GUI Filre : Prune ( Used to architect the testbench using a GUI )
<br />

  - Basic GUI frame added
  - Basic GUI directory and the main python file uploaded
  - The Treeview file/architecture structure has been added.
  - Generic testbench layout is loaded from an external file which will be set to read only
