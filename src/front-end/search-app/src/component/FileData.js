import React from 'react'

function FileData(props){ 
    if (props.data.selectedFiles) { 
      return ( 
        <div> 
          <hr />
          <h2>Files Uploaded:</h2>
          <ul>
            <li>{props.data.selectedFiles.filename}</li>
          </ul>
        </div> 
      )
    } else { 
      return ( 
        <div> 
          <hr /> 
          <h4>No files has been uploaded</h4> 
        </div> 
      )
    } 
}

export default FileData