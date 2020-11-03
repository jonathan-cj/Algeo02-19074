import React from 'react'

function FileData(props){ 
    if (props.selectedFiles) { 
      return ( 
        <div> 
          <h2>File Details:</h2> 
          
        </div> 
      )
    } else { 
      return ( 
        <div> 
          <br /> 
          <h4>Choose before Pressing the Upload button</h4> 
        </div> 
      )
    } 
}

export default FileData