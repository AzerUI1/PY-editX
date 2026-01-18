const editor = document.getElementById('editor');

const boldBtn = document.getElementById('boldBtn');
const italicBtn = document.getElementById('italicBtn');
const underlineBtn = document.getElementById('underlineBtn');
const strikeBtn = document.getElementById('strikeBtn');

const alignLeft = document.getElementById('alignLeft');
const alignCenter = document.getElementById('alignCenter');
const alignRight = document.getElementById('alignRight');

const fontSizeUp = document.getElementById('fontSizeUp');
const fontSizeDown = document.getElementById('fontSizeDown');

const downloadBtn = document.getElementById('downloadBtn');
const editBtn = document.getElementById('editBtn');
const downloadAppBtn = document.getElementById('downloadAppBtn');

const wordCount = document.getElementById('wordCount');
const charCount = document.getElementById('charCount');
const cursorPosition = document.getElementById('cursorPosition');

function formatText(command, value = null) {
    document.execCommand(command, false, value);
    editor.focus();
}

function updateCounts() {
    const text = editor.innerText;
    const words = text.trim() ? text.trim().split(/\s+/).length : 0;
    const chars = text.length;

    wordCount.textContent = words + " words";
    charCount.textContent = chars + " characters";
}

function updateCursorPosition() {
    const selection = window.getSelection();
    if (!selection.rangeCount) return;

    const range = selection.getRangeAt(0);
    const preRange = range.cloneRange();
    preRange.selectNodeContents(editor);
    preRange.setEnd(range.endContainer, range.endOffset);

    const text = preRange.toString();
    const lines = text.split("\n");

    const line = lines.length;
    const column = lines[lines.length - 1].length + 1;

    cursorPosition.textContent = "Line " + line + ", Column " + column;
}

function downloadText() {
    const text = editor.innerText;
    const blob = new Blob([text], { type: 'text/plain' });
    const url = URL.createObjectURL(blob);

    const a = document.createElement('a');
    a.href = url;
    a.download = "document.txt";
    a.click();

    URL.revokeObjectURL(url);
}

function downloadApp() {
    alert("This would download the editX desktop app in a real project.");
}

function toggleEdit() {
    const isEditing = editor.contentEditable === 'true';
    editor.contentEditable = isEditing ? 'false' : 'true';
    editBtn.innerHTML = isEditing ? '<i class="fas fa-edit"></i> Edit' : '<i class="fas fa-save"></i> Save';
}

boldBtn.onclick = () => formatText("bold");
italicBtn.onclick = () => formatText("italic");
underlineBtn.onclick = () => formatText("underline");
strikeBtn.onclick = () => formatText("strikeThrough");

alignLeft.onclick = () => formatText("justifyLeft");
alignCenter.onclick = () => formatText("justifyCenter");
alignRight.onclick = () => formatText("justifyRight");

fontSizeUp.onclick = () => formatText("fontSize", "5");
fontSizeDown.onclick = () => formatText("fontSize", "3");

downloadBtn.onclick = downloadText;
editBtn.onclick = toggleEdit;
downloadAppBtn.onclick = downloadApp;

editor.addEventListener("input", updateCounts);
editor.addEventListener("keyup", updateCursorPosition);
editor.addEventListener("mouseup", updateCursorPosition);

updateCounts();
