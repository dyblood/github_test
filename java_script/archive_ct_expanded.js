function Archive_CT_Expanded() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('CT EXPANDED'); //source sheet
    var testrange = sheet.getRange('X:X'); //range to check
    var testvalue = (testrange.getValues());
    var csh = ss.getSheetByName('CT ARCHIVE'); //destination sheet
    var data = [];
    var j =[];
  
    //Condition check in H:H; If true copy the same row to data array
  for (i=0; i<testvalue.length;i++) {
    if ( testvalue[i] == 'X') {
    data.push.apply(data,sheet.getRange(i+1,1,1,25).copyTo(csh.getRange(csh.getLastRow()+1,1,1,25)));
    //Copy matched ROW numbers to j
    j.push(i);
   }
   }
  
   //csh.getRange(csh.getLastRow()+1,1,data.length,data[0].length).setValues(data);
  
  //Delete matched rows in the source sheet
    for (i=0;i<j.length;i++){
    var k = j[i]+1;
    sheet.deleteRow(k);
  
  //Alter j to account for deleted rows
    if (!(i == j.length-1)) {
    j[i+1] = j[i+1]-i-1;
  }
  }
  }
  //---------------------------------------------------------------------------------------------------------------
  function Archive_Current() {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('Current'); //source sheet
    var testrange = sheet.getRange('I:I'); //range to check
    var testvalue = (testrange.getValues());
    var csh = ss.getSheetByName('Completed'); //destination sheet 1
    var csh2 = ss.getSheetByName('RETURNED AMA'); //destination sheet 2
    var data = [];
    var j =[];
  
    //Condition check in W:W; If true copy the same row to data array
  for (i=0; i<testvalue.length;i++) {
    if ( testvalue[i] == 'RTD 600 SENT') {
      data.push.apply(data,sheet.getRange(i+1,1,1,25).copyTo(csh.getRange(csh.getLastRow()+1,1,1,25)));
    //Copy matched ROW numbers to j
    j.push(i);
   }
    if ( testvalue[i] == 'RETURNED AMA') {
      data.push.apply(data,sheet.getRange(i+1,1,1,25).copyTo(csh2.getRange(csh2.getLastRow()+1,1,1,25)));
    //Copy matched ROW numbers to j
    j.push(i);
   }
   }
  //Copy data array to destination sheet
  
   //csh.moveRows.getRange(csh.getLastRow()+1,1,data.length,data[0].length);
  
  //Delete matched rows in the source sheet
    for (i=0;i<j.length;i++){
    var k = j[i]+1;
    sheet.deleteRow(k);
  
  //Alter j to account for deleted rows
    if (!(i == j.length-1)) {
    j[i+1] = j[i+1]-i-1;
  }
  }
  }
  //----------------------------------------------------------------------------------------------------------------
  //----------------------------------------------------------------------------------------------------------------
  /*function lookupCC(){
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName('CT EXPANDED');
    var testrange = sheet.getRange('A:A');
    var testvalue = (testrange.getValues());
    var targetSheet = ss.getSheetByName('CT ARCHIVE');
    var data = [];
    var j = [];
  
    
  }*/
  
  
  
  
  
  
  
  //Adding Menu tab.----------------------------------------------------------------------------------------------------
  /*function addMenu()
  {
    var menu = SpreadsheetApp.getUi().createMenu('YB_Scripts');
    menu.addItem('ArchiveRows', 'copyrange');
    menu.addToUi(); 
  }
  
  function onOpen(e){
    addMenu();
  }*/