# Search App
> Tugas Besar 2 IF 2123 Aljabar Linier dan Geometri Aplikasi Dot Product pada Sistem Temu-balik Informasi Semester I Tahun 2020/2021


## Table of contents
* [General info](#general-info)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Inspiration](#inspiration)

## General info
Temu-balik informasi(_information retrieval_) merupakan proses menemukan kembali (_retrieval_) informasi yang relevan terhadap kebutuhan pengguna dari suatu kumpulan informasi secara otomatis. Biasanya, sistem temu balik informasi ini digunakan untuk mencari informasi pada iformasi yang tidak terstruktur, seperti laman web atau dokumen. _Search-engine_ ini merupakan sebuah aplikasi _dot product_ pada sistem temu-balik informasi yang menggunakan model ruang vektor dan memanfaatkan _cosine similarity_.

## Screenshots

Landing Page

![LandingPage](https://user-images.githubusercontent.com/63598464/98943479-24b6af00-2522-11eb-9602-dd63b559c5e2.jpg)

Result of a Query

![result](https://user-images.githubusercontent.com/63598464/98943559-46b03180-2522-11eb-9502-fbbad5d4bf36.jpg)

## Setup
1. Clone Repo
```javascript
git clone https://github.com/jonathan-cj/Algeo02-19074
```
2. Start Back-End dan Front-End
```javascript
cd Algeo02-19074
cd src
```
```javascript
cd front-end/search-app
yarn start
```
```javascript
cd ../..
cd back-end
flask run
```
3. Buka Localhost
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
![LandingPage](https://user-images.githubusercontent.com/63598464/98943479-24b6af00-2522-11eb-9602-dd63b559c5e2.jpg)

Berikut merupakan contoh penggunaan dari _search-engine_,
![Run](https://user-images.githubusercontent.com/63598464/98943899-c9d18780-2522-11eb-8b33-8af6ecabc0ca.gif)

## Features
List of features
* _Similarity_ antara _Query_ dan Dokumen
* Tabel _Term_ dan Banyak Kemunculan _Term_

## Status
Project is: _in progress_

## Inspiration
[Tugas Besar 2 Aljabar dan Geometri](https://informatika.stei.itb.ac.id/~rinaldi.munir/AljabarGeometri/2020-2021/Tubes2-Algeo-2020.pdf)
