import React from "react"
import "../App.css"

function File(props){
    var link = "localhost:5000/database/"
    return(
        <div className="File">
            <a href={link.concat(props.file.filename)} target="_blank" className="App-link">
                <h4>{props.file.title}</h4>
            </a>
            <p>Jumlah kata: {props.file.totalword}</p>
            <p>Tingkat kemiripan: {Math.round(props.file.similiarity*100)/100}%</p>
            <p>"{props.file.firstsentence}"</p>
        </div>
    )
}

export default File