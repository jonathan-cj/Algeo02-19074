import React from "react"
import "../App.css"

function File(props){
    var link = "localhost:5000/database/"
    return(
        <a href={link.concat(props.file.filename)} target="_blank" rel="noreferrer" style={{textDecoration:"none"}}>
            <div className="File">
                <h4 className="App-link">{props.file.title}</h4>
                <p>Jumlah kata: {props.file.totalword}</p>
                <p>Tingkat kemiripan: {Math.round(props.file.similiarity*100)/100}%</p>
                <p>"{props.file.firstsentence}"</p>
            </div>
        </a>
    )
}

export default File