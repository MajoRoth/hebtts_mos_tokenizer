function doGet(e) {

	var params = e.parameter;
	var SpreadSheet = SpreadsheetApp.openById("1CGzBVOT460e8rWHAe1jCbUZhm1BgBJIv22-AFUnK4HM");
	var Sheet = SpreadSheet.getSheets()[0];
	var LastRow = Sheet.getLastRow();

	Sheet.getRange(LastRow+1, 1).setValue(params.name);
	Sheet.getRange(LastRow+1, 2).setValue(params.mail);
	Sheet.getRange(LastRow+1, 3).setValue(params.formid);

  // robo
  for (var i = 1; i <= 5; i++) {
		Sheet.getRange(LastRow+1, 3+i).setValue(params["robo" + i.toString()]);
	}
  // mms
  for (var i = 1; i <= 5; i++) {
		Sheet.getRange(LastRow+1, 8+i).setValue(params["mms" + i.toString()]);
	}

  // valle (words)
  for (var i = 1; i <= 5; i++) {
		Sheet.getRange(LastRow+1, 13+i).setValue(params["words" + i.toString()]);
	}

  // valle (alephbert)
  for (var i = 1; i <= 5; i++) {
		Sheet.getRange(LastRow+1, 18+i).setValue(params["alephbert" + i.toString()]);
	}


    console.log("done")
	return ContentService.createTextOutput(params.thank);
}