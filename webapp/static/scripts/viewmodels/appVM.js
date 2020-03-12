'strict';
var host = location.protocol + '//' + location.hostname + (location.port ? ':' + location.port : '');

//Main Application ViewModel
function App() {
    _self = this;
    this.Tasks = new ko.observableArray([]);

}

//Get tasks from todoist Tech project, populating the Tasks observable array
App.prototype.getTasks = function () {
    fetch(host + '/gettasks')
        .then(function (response) {
            if (response.ok)
                return response.json();
            
        }).then(function (response) {
            if (response.data.tasks) {
                const tasks = response.data.tasks;
                tasks.forEach(task => _self.Tasks.push(task));
            }                
        });

};