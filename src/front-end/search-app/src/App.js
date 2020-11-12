import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';
import axios from 'axios'

import Main from './component/Main'
import Upload from './component/Upload'
import Header from './component/Header'
import FileData from './component/FileData'
import File from './component/File'

class App extends Component  {
  constructor(){
    super()
    this.state = {
      searchQuery: null,
      search: false,
      selectedFiles: undefined,
      results: [],
      uploadedFiles: [],
      tableData: []
    }
    this.HandleChange = this.HandleChange.bind(this)
    this.HandleSearch = this.HandleSearch.bind(this)
    this.onFileChange = this.onFileChange.bind(this)
    this.HandleSubmit = this.HandleSubmit.bind(this)
    this.upload = this.upload.bind(this)
    this.CreateTable = this.CreateTable.bind(this)
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

    this.setState({
      results: []
    })

    var param = {
      query:this.state.searchQuery
    }

    axios.post(`/search/`, param)
      .then(res => {
        console.log(res);
        console.log(res.data);
        const results = res.data
        this.setState({ results })
      })
      
    axios.post(`/table`,param)
      .then(res => {
        console.log(res.data)
        const tableData = res.data
        this.setState({ tableData })
      })

    this.setState({
      search: true
    })
  }

  //Mengubah state selectedFiles ketika ada file yang dipilih
  onFileChange(event){
    this.setState({
      selectedFiles: event.target.files
    })
    console.log(this.state.selectedFiles)
  }

  //Upload file ke backend server
  upload(file){
    const data = new FormData()
    data.append("file", file)
    axios.post("/upload", data)
    .then(res => {
      console.log(res.statusText)
    })
  }

  //Submit files
  HandleSubmit(event){
    event.preventDefault()
    const selectedFiles = this.state.selectedFiles
    const uploadedFiles = []

    for(let i=0; i<selectedFiles.length; i++){
      this.upload(selectedFiles[i])
      uploadedFiles.push(selectedFiles[i])
    }

    this.setState({ uploadedFiles })
  }

  //Buat tabel jumlah kata
  CreateTable(column){
    const component = column.map(props => <td>{props}</td>)
      return(
        <tr width="100px">
          {component}
        </tr>
      )
    }

  render(){//Tampilan web
    this.state.results.sort((a,b) => a.similiarity>b.similiarity ? -1 : 1) 
    const searchResult = this.state.results.map(file => <File key={file.title} file={file}/>)

    if (this.state.results.length !== 0 && this.state.search) {
      var table = this.state.tableData.map(this.CreateTable)
    }

    const scroll = {
      overflowX:'auto'
    }
    return (
      this.state.search ?
        this.state.results.length!==0 ?
          <div className="Header">
            <Header 
              HandleChange={this.HandleChange} 
              HandleSearch={this.HandleSearch}
              data={this.state}
            />
            <h4>Upload more files :</h4>
            <Upload 
              HandleSubmit={this.HandleSubmit}
              HandleChange={this.onFileChange}
            />
            <hr className="Line"/>
            <h4>Top search results :</h4>
            {searchResult}
            <h4>Query Total per Files:</h4>
            <div style={scroll}>
              <table>{this.state.tableData.length!==0 ? table:null}</table>
            </div>
            <hr className="Line"/>
            <a href="https://google.com" target="_blank" rel="noreferrer" className="App-link">
              PERIHAL BLOM ADA
            </a>
          </div>
        :
          <div className="App">
            <header className="App-header">
              <img src={logo} className="App-logo" alt="logo" />
              <h>Searching...</h>
            </header>
          </div>
      :   
        <div className="App">
          <header className="App-header">
            <img src={logo} className="App-logo" alt="logo" />
            <Main 
              HandleChange={this.HandleChange} 
              HandleSearch={this.HandleSearch}
              data={this.state} 
            />
            <br />
            <hr className="Line-main"/>
            <Upload 
              HandleSubmit={this.HandleSubmit}
              HandleChange={this.onFileChange}
            />
            <FileData 
              data={this.state}
            />
          </header>
        </div>
    )}
}

export default App;
