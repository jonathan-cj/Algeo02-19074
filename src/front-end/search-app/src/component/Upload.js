import React from 'react'

function Upload(props){
    return(
        <form onSubmit={props.HandleSubmit} method="post">
            <input 
                onChange={props.HandleChange} 
                type="file" 
                multiple
            />
            <button>Upload</button>
        </form>
    )
}

export default Upload