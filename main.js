const path = require('path');
const { app, BrowserWindow } = require('electron');
const {PythonShell} = require('python-shell');
//const test = require('./app/scripts/test.js');

function createMainWindow()
{
    const mainWindow = new BrowserWindow
    ({
            title: 'LastFM RPC',
            width: 800,
            height: 510,
            autoHideMenuBar: true,
            webPreferences: {
                nodeIntegration: true,
                contextIsolation: false,
            }
        })
        

    
        mainWindow.loadFile(path.join(__dirname, './app/index.html'));
}

app.whenReady().then(() =>{ 
    // Start the main Python script
     mainPyshell = new PythonShell('app\\scripts\\lyricsBoi.py');

    // Start the server Python script
    createMainWindow()
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow()
        }
    })
});

app.on('window-all-closed', () => {
    if (process.platform !== 'darwin') {
        app.quit()
    }
})
