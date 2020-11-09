import React from "react"
import "../App.css"

function Header(props){
    return(
        <form onSubmit={props.HandleSearch}>
          <input 
            className="Search-bar"
            type="text" 
            value={props.data.searchQuery}
            name="searchQuery" 
            placeholder="Search..." 
            onChange={props.HandleChange} 
          />
          <button className="Search-button">Search</button>
        </form>
    )
}

export default Header