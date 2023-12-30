function clearText(){
  document.querySelector('textarea').value = "" ;
}

function validSubmission(){
  var text = document.querySelector('textarea').value;
  if (text.trim() == ''){
    alert("Missing the content !!!,<br> Please parse the news article before proceed.");
    return false;
  }
  return true;
} 

function hideMsg(){
  var msgBox = document.getElementById('msgbox');
  msgBox.classList.add('hide');
}
