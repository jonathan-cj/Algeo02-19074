import React from "react"
import "../App.css"

function Header(props){
    return(
        <form className="Header" onSubmit={props.HandleSubmit}>
          <input 
            className="search"
            type="text" 
            value={props.data.searchQuery}
            name="searchQuery" 
            placeholder="Search..." 
            onChange={props.HandleChange} 
          />
          <button className="searchButton">Search</button>
        </form>
    )
}

export default Header