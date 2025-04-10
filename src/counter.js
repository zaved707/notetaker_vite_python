export async function getFiles() {
    try {
      const response = await fetch('/api/items')
      const data = await response.json()
      return data
    } catch (error) {
      console.error('Error fetching items:', error)
      throw error // Optionally rethrow the error for the caller to handle
    }
  }
  export async function getContent(fileName){
    const response = await fetch(`/api/fetchFile?filename=${fileName}`)
  const data = await response.json()
  return data
  }

 export async function saveFileToServer(fileContent, fileName) {
    // Construct the URL with query parameters
    const url = `/api/saveFile?fileContent=${encodeURIComponent(fileContent)}&fileName=${encodeURIComponent(fileName)}`;
    
    // Make the GET request using fetch
    fetch(url)
        .then(response => {
            // Check if the response is OK (status 200-299)
            if (!response.ok) {
              console.log( response.json(),'this is reposnse'); 
                throw new Error(`HTTP error! Status: ${response.status}`);
                
            }
          // Parse the JSON response
        })
        .then(data => {
            // Handle the successful response
            console.log('File saved successfully:', data);
        })
        .catch(error => {
            // Handle errors (e.g., network issues or server errors)
            console.error('Error saving file:', error);
        });
}