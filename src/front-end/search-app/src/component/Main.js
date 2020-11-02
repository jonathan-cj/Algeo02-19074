import React from "react"
import "../App.css"

function Main(props){
    return(
        <form className="Main" onSubmit={props.HandleSubmit} method="post">
          <input 
            type="text" 
            value={props.data.searchQuery}
            name="searchQuery" 
            placeholder="Search..." 
            onChange={props.HandleChange} 
          />
          <button>Search</button>
        </form>
    )
}

export default Main