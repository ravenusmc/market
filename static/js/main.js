
//This function will ensure that the user enter the correct value. 
function validate() {

  var kale = document.getElementById('kale').value;
  var collards = document.getElementById('collards').value;
  var broccoli = document.getElementById('broccoli').value;
  var spinach = document.getElementById('spinach').value;

  if (isNaN(kale)) {
    alert('Please enter a valid number for the Kale selection.');
    return false;
  } else if (isNaN(collards)){
    alert('Please enter a valid number for the collards selection.')
    return false;
  } else if (isNaN(broccoli)){
    alert('Please enter a valid number for the broccoli selection.')
    return false;
  } else if (isNaN(spinach)){
    alert('Please enter a valid number for the broccoli selection.')
    return false;
  }

  return true;
}
