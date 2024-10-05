const { Given, When, Then } = require('cucumber');
const { exec } = require('child_process');

Given('a application', function () {
    console.log('application is ready to be launched.');
});

When('I launch the application', function (callback) {
    exec('bash -c "ping remoteHost"', (error, stdout, stderr) => {
        if (error) {
            console.error(`exec error: ${error}`);
            return callback(error);
        }
        console.log(`stdout: ${stdout}`);
        console.error(`stderr: ${stderr}`);
        callback();
    });
});

Then('the application should run successfully', function () {
    console.log('Application ran successfully.');
});