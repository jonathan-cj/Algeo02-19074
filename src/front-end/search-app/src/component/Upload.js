import React from 'react'

function Upload(){
    return(
        <form>
            <input type="file" id="myfile" multiple name="myfile"></input>
            <button>Upload</button>
        </form>
    )
}

export default Upload