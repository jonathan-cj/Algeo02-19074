import React from "react"
import "../App.css"

function File(props){
    return(
        <div>
            <h2>Nama File: {props.file.name}</h2>
            <p>Nama Type: {props.file.type}</p>
        </div>
    )
}

export default File