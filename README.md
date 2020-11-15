# Search App
> Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri Aplikasi Dot Product pada Sistem Temu-balik Informasi Semester I Tahun 2020/2021


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [References](#References)
* [About Us](#about-us)

## General info
Temu-balik informasi(_information retrieval_) merupakan proses menemukan kembali (_retrieval_) informasi yang relevan terhadap kebutuhan pengguna dari suatu kumpulan informasi secara otomatis. Biasanya, sistem temu balik informasi ini digunakan untuk mencari informasi pada iformasi yang tidak terstruktur, seperti laman web atau dokumen. _Search-engine_ ini merupakan sebuah aplikasi _dot product_ pada sistem temu-balik informasi yang menggunakan model ruang vektor dan memanfaatkan _cosine similarity_.

## Screenshots

Landing Page

![landingPage](https://user-images.githubusercontent.com/63598464/99136022-79a71200-2655-11eb-906a-bf12f7dde580.jpg)

Result of a Query

![resultQuery](https://user-images.githubusercontent.com/63598464/99136028-7ca20280-2655-11eb-8917-ccdb48625bd0.jpg)

Table of Terms

![tableTerm](https://user-images.githubusercontent.com/63598464/99136032-80358980-2655-11eb-8506-e424f7b16283.jpg)

## Prerequisites
* [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/)
* [NodeJS](https://nodejs.org/en/)
* [Yarn](https://yarnpkg.com/)

## Setup
1. Clone Repo
```javascript
git clone https://github.com/jonathan-cj/Algeo02-19074
```
2. Start Front-End
```javascript
cd Algeo02-19074/src/front-end/search-app
yarn start
```
![front-end](https://user-images.githubusercontent.com/63598464/99136402-2a61e100-2657-11eb-8a5c-fe216d1ac231.gif)

Jika menemukan error berikut ketika melakukan yarn start, 
![image](https://user-images.githubusercontent.com/63598464/99066266-4031c080-25db-11eb-86ed-973e7f0f5ae9.png)

Jalankan perintah berikut sebelum melakukan yarn start kembali
```javascript
npm update
```

3. Start Back-End

  Buka terminal baru dan direktori tempat dilakukannya git clone
```javascript
cd Algeo02-19074/src/back-end
flask run
```
![back-end](https://user-images.githubusercontent.com/63598464/99135710-55e3cc00-2655-11eb-928b-510189137729.gif)

4. Buka Localhost
```javascript
http://localhost:3000/
```

## How To Use
Berikut ini adalah input yang akan dimasukkan pengguna untuk eksekusi program.
1. __Search query__, berisi kumpulan kata yang akan digunakan untuk melakukan
pencarian
1. __Kumpulan dokumen__, dilakukan dengan cara mengunggah multiple file ke
dalam web browser.
Tampilan layout dari aplikasi web yang akan dibangun adalah sebagai berikut.
![landingPage](https://user-images.githubusercontent.com/63598464/99136022-79a71200-2655-11eb-906a-bf12f7dde580.jpg)

Berikut merupakan contoh penggunaan dari _search-engine_, sebelum _upload_ dokumen pastikan folder test kosong,

![ezgif com-gif-maker](https://user-images.githubusercontent.com/63598464/99137509-d73f5c80-265d-11eb-87b7-e25667aba5a9.gif)

## Features
List of features
* _Similarity_ antara _Query_ dan Dokumen
* Tabel _Term_ dan Banyak Kemunculan _Term_

## Status
Project is: _in progress_

## References
1. [Tugas Besar 2 Aljabar dan Geometri](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Tubes2-Algeo-2020.pdf)
2. [Aplikasi Dot-Product pada Sistem Temu Balik Informasi](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Algeo-12-Aplikasi-dot-product-pada-IR.pdf)

## About Us
Mahasiswa Teknik Informatika Peserta Kuliah IF2123 Tahun Ajaran 2020/2021
1. Christopher Chandrasaputra - 13519074
2. Isabella Handayani Sumantri - 13519081
3. Jonathan Christhoper Jahja - 13519144
