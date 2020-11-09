import React from "react"
import "../App.css"

function File(props){
    return(
        <div>
            <h2>{props.file.title}</h2>
            <p>Jumlah kata:</p>
            <p>Tinkgat kemiripan</p>
            <p>Kalimat Pertama</p>
        </div>
    )
}

export default File