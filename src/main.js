console.log("loaded script");

import "./style.css";
import { getFiles,getContent,saveFileToServer} from "./counter.js";


function clearPage(){
  const container = document.getElementById("pageListContainer");
  container.innerHTML='';
}

async function addPage(pageName) {
  const container = document.getElementById("pageListContainer");
  const li = document.createElement("li");
  const a = document.createElement("a");
  a.href = "#"; // Same as the original
  a.textContent = pageName || "Unnamed Page"; // Use custom name or fallback
  // a.id = `${pageName.toLowerCase().replace(/\s+/g, '')}Button` // Generate unique ID
  a.addEventListener('click',async function() {
    const content = await getContent(pageName);
    console.log(content)
    showContent( pageName,content.message)
  })
  li.appendChild(a);
  container.appendChild(li);
}



function showContent(pageName,content) {
  const title=document.getElementById('fileTitle')
  title.textContent=pageName
  editor.value(content)
  console.log(typeof editor.value())
 
}

function currrentPage(){
  return document.getElementById('fileTitle').textContent;
}

function createNewFile(name){
  saveFileToServer(`${name}`,name)      // TODO : Make it work without the space(there should be no space required to create a new file so that the new file is truly empty)
  initialise()
}

async function initialise(){
  const result = await getFiles()
  console.log(result)
  clearPage()
  result.items.forEach(page => {
    addPage(page)
  })
} 

function getEditorvalue(){
  return editor.value();
}
const saveButton=document.getElementById('saveButton')
initialise();
const editor = new EasyMDE({ element: document.getElementById('editor1') });

editor.value('# fuck ths shit')
saveButton.addEventListener('click',()=> {
  let content = getEditorvalue()
  console.log(content)
 
  saveFileToServer(content,currrentPage())
})

const createFileButton=document.getElementById('createFileButton');
createFileButton.addEventListener('click',()=>{
  let fileName=document.getElementById('newFileNameTextbox').value;
  createNewFile(fileName)
  console.log('createFileButton pressed')
})
// const editor2 = new EasyMDE({ element: document.getElementById('editor2') });
