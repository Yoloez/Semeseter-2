var angka1 = document.getElementById("num1");
var angka2 = document.getElementById("num2");

function tambah() {
  var hasil = parseInt(angka1.value) + parseInt(angka2.value);
  document.getElementById("result").innerHTML = "Hasil: " + hasil;
}

function kurang() {
  var hasil = parseInt(angka1.value) - parseInt(angka2.value);
  document.getElementById("result").innerHTML = "Hasil: " + hasil;
}

function kali() {
  var hasil = parseInt(angka1.value) * parseInt(angka2.value);
  document.getElementById("result").innerHTML = "Hasil: " + hasil;
}

function bagi() {
  var hasil = parseInt(angka1.value) / parseInt(angka2.value);
  document.getElementById("result").innerHTML = "Hasil: " + hasil;
}

function cek() {
  var operator = document.getElementById("operator");

  switch (operator.value) {
    case "+":
      tambah();
      break;
    case "-":
      kurang();
      break;
    case "*":
      kali();
      break;
    case "/":
      bagi();
      break;
    default:
      document.getElementById("result").innerHTML = "Operator tidak valid";
      break;
  }
}
