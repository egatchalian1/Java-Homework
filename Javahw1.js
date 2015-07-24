
//1.
var numbers = 1 + 2 + 3; //this sum to 6
var numbers2 = '1' + 2 + 3//since 1 is a string 2 and 3 will sum up to 5, becoming 15
var numbers3 = '123' + '123'// '123' is a string so it will print out both side by side 123123
var numbers4 = 123 + 123; // this will add up to 246 they're  numbers adding

//2.
var count = '34.908';
var countNum = parseInt(count);
var countNum1 = parseFloat(count);

alert(countNum);
alert(countNum1);
// to get the 34.908, you will have to make it parseFloat


//3.
var age = 702;

alert('age'.length);
// to get the number 3 like we wanted, .length is for strings so it didn't work for 702 but it works for 'age'


//4.
var age = prompt("Please Enter your age")
if (age > 18 && age <25) {
    alert("You're the perfect age!");
} else if ( age < 18 ) {
    alert("You're too young.");
} else if (age > 25 ) {
	alert("You're too old");
}
// alert box with age
