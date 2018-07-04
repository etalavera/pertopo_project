const regexNumbers = /[0-9]/gm;
function goTo(id) {
  window.location.has = '#' + id;
}

function onlyNumbers(key, o) {
  var array = key.split('');
  for(var i=0; i<array.length; i++) {
    if (regexNumbers.exec(array[i]) == null) {
      array[i] = ""
    }
  }
  array.join()
  o.value = array.toString();
}
