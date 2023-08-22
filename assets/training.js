let a = 34;
let b = 454;

console.log(typeof a);
let c = 50;
const d = 43;

let z = (c % a) * (c - d);

console.log("alert");
console.log(z++);

let e;
console.log(typeof e); //fungsi typeof untuk memastikan tipedata pada variabel untuk mengembalikan tipe data dalam bentuk teks //undefined (Tidak memiliki nilai pada terdefinisi dari tipe data)

// if (e >= 50){
//     console.log("My Logi ",  e)
// } else if (e <= 20){
//     console.log("Selamat pagi", e);
// } else if (e <= 4){
//     console.log("Ayo mi" , e)
// }
let char1 = "Kak Sadno";
let char2 = "Adrian";
let language1 = "Indonesia";
let language2 = "English";

let greeting = null;
let greeting1 = null;

switch (language2) {
  case "Indonesia":
    greeting = "Javanese";
    break;
  case "Japanese":
    greeting = "Konnichiwa";
    break;
  case "English":
    greeting = "Good morning";
    break;
  default:
    greeting = "Selamat pagi";
}
console.log(greeting);

// let fruits = ["Mango", "Apple", "kiwi", "Grape", "Pir", "Orange", "Lychee", "Guava", "Papaya", "Mustmelon", "Watermelon", "Blueberry", "Sunsettia"];
// for (let i= 0; i< 5; i++) {
//     console.log(i)

// }
// console.log("")
// for (const arrayItem of fruits) {
//     console.log(arrayItem)

// }

// let firstName = "Devon";
// let lastName = "Pakilaran";
// let age = 20;
// let isMarried = true;



score = 10;
// * Buatlah logika if untuk mengevaluasi nilai score dengan ketentuan:
// *  1. Jika score bernilai 90 atau lebih
// *      - Isi variabel result dengan nilai: 'Selamat! Anda mendapatkan nilai A.'
// *  2. Jika score bernilai 80 hingga 89
// *      - Isi variabel result dengan nilai: 'Anda mendapatkan nilai B.'
// *  3. Jika score bernilai 70 hingga 79
// *      - Isi variabel result dengan nilai: 'Anda mendapatkan nilai C.'
// *  4. Jika score bernilai 60 hingga 69:
// *      - Isi variabel result dengan nilai: 'Anda mendapatkan nilai D.'
// *  5. Jika score bernilai di bawah 60:
// *      - Isi variabel result dengan nilai: 'Anda mendapatkan nilai E.'
// if (score >= 90){
//     console.log("Selamat! Anda mendapatkan Nilai A");
// } else if (score >= 80 && score <= 89){
//     console.log("Anda mendapatkan nilai B");
// } else if (score >= 70 && score <= 79){
//     console.log("Anda mendapatkan nilai C");
// } else if (score >= 60 && score <= 69){
//     console.log("Anda mendapatkan nilai D");
// } else if (score < 60 ){
//     console.log("Anda mendapatkan nilai E");
// } else {
//     console.log("Maaf anda tidak Lulus");
// } return score;
// console.log(score);
const user = {name: "Devon", age: 30, fakultas: "MIPA", isJedi: true};
const admin = {name: "Adrian", age: 22, fakultas: "MIPA", isName: true};

const user2 = {firsName : "Fauzi", lastName:"Kimochi", fakultas: "MIPA", prodi :"Sistem Informasi",isDerek: true,
 };
console.log(`Halo nama saya ${user.name} dan umur saya ${user.age}`);
console.log(`Fakultas saya ${user.fakultas} dan Prodi Saya ${user2.prodi} serta ${user2["GotoMall"]}`);

let myArray = ["Fatwa", "Devon", "Alif", "Fajri", "Arden"];
let myArray2 = [20, 34, 55,44, 12, 34,43];

console.log(myArray, myArray2);

const user3 = {firstName : "Devon", lastName : "Pakilaran", isLOL: true, "OnMyWay": "Hall", };

let user11 = {firstName : "Bearer", lastName: "Pakilaran", isThat:true, "Banyak": "Only much"};
console.log(...myArray, ...myArray2);
console.log({...user, ...user2, ...user3});

let firsName = user11.firstName
let lastName = user11.lastName
console.log(firsName, lastName);

const favourite = ["Games", "Food and beverage", "Anime", "CSGO", 54, 434.5];

const  [firstGames, secondFood, thirdAnime, fourthGames, fifthFood, sixthNumber]= favourite;

console.log(favourite);
console.log(firstGames);
console.log(secondFood);
console.log(thirdAnime);
console.log(fourthGames);
console.log(fifthFood);
console.log(sixthNumber)

console.log("Hello World");
let namadepan = "Skywalker";
const namabelakang = "depan";
console.log(namadepan);
console.log(namabelakang);
  