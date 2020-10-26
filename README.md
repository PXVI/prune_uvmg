# uvmg_alpha
Automated custom configurable UVM Test Environment generation tool ( terminal &amp; gui supported )<br /><br />

### Updates

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
