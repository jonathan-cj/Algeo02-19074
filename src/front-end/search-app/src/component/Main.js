import React from "react"
import "../App.css"

function Main(props){
    return(
        <form className="Main" onSubmit={props.HandleSearch} method="post">
          <input 
            type="text" 
            value={props.data.searchQuery}
            name="searchQuery" 
            placeholder="Search..." 
            onChange={props.HandleChange} 
            formtarget="_self"
            className="Search-bar"
          />
          <button className="Search-button">Search</button>
        </form>
    )
}

export default Main