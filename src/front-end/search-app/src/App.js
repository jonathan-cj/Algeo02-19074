import logo from './logo.svg';
import './App.css';
import React, {Component} from 'react';
import axios from 'axios'

import Main from './component/Main.js'

class App extends Component  {
  constructor(){
    super()
    this.state = {
      searchQuery: null,
      submit: false,
    }
    this.HandleChange = this.HandleChange.bind(this)
    this.HandleSubmit = this.HandleSubmit.bind(this)
  }

  HandleChange(event){
    const {name, value} = event.target
    this.setState({
      [name]: value
    })
  }

  HandleSubmit(event){
    event.preventDefault()
    const query = event.searchQuery

    axios.post(`/query`, { query })
      .then(res => {
        console.log(res);
        console.log(res.data);
      })
  }

  render(){
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <Main 
            HandleChange={this.HandleChange} 
            HandleSubmit={this.HandleSubmit}
            data={this.state} 
          />
        </header>
      </div>
    )}
}

export default App;
