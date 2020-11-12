import React from 'react'

function FileData(props){ 
    if (props.data.uploadedFiles.length!==0) { 
      return ( 
        <div className="File-list"> 
          <h3>Files Uploaded:</h3>
          <ul>
            {props.data.uploadedFiles.map(file => <li>{file.name}</li>)}
          </ul>
        </div> 
      )
    } else { 
      return ( 
        <div className="File-list"> 
          <h4>No files has been uploaded recently</h4> 
        </div> 
      )
    } 
}

export default FileData