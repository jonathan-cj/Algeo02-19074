import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';
import axios from 'axios'

import Main from './component/Main'
import Upload from './component/Upload'
//import File from './component/File'

class App extends Component  {
  constructor(){
    super()
    this.state = {
      searchQuery: null,
      submit: false,
      selectedFiles: null
    }
    this.HandleChange = this.HandleChange.bind(this)
    this.HandleSearch = this.HandleSearch.bind(this)
    this.onFileChange = this.onFileChange.bind(this)
    this.HandleSubmit = this.HandleSubmit.bind(this)
  }

  //Update state dengan searchQuery yang baru
  HandleChange(event){
    const {name, value} = event.target
    this.setState({
      [name]: value
    })
  }

  //Mengirim data searchQuery ke backend server
  HandleSearch(event){
    event.preventDefault()
    var param = {
      query:this.state.searchQuery
    }

    axios.post(`/search/`, param)
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  //Mengubah state selectedFiles ketika ada file yang dipilih
  onFileChange(event){
    this.setState({
      selectedFiles:event.target.files[0]
    })
    console.log(this.state.selectedFiles)
  }

  //Upload files ke backend server
  HandleSubmit(event){
    event.preventDefault()
    const data = new FormData()
    data.append('file', this.state.selectedFiles)
    axios.post("/upload", data)
    .then(res => {
      console.log(res.statusText)
    })
  }

  render(){//Tampilan web
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Main 
            HandleChange={this.HandleChange} 
            HandleSearch={this.HandleSearch}
            data={this.state} 
          />
          <Upload 
            HandleSubmit={this.HandleSubmit}
            HandleChange={this.onFileChange}
          />
        </header>
      </div>
    )}
}

export default App;
