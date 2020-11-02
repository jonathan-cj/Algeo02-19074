import React from "react"
import "../App.css"

function File(props){
    return(
        <div className="File">
            <h2>{props.file.name}</h2>
            <p>{props.file.desc}</p>
        </div>
    )
}

export default File