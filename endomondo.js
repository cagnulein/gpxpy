require('cross-fetch/polyfill');
const fs = require('fs');
const { Api } = require('endomondo-api-handler');
 
const api = new Api();
 
(async () => {
    await api.login('EMAIL', 'PASSWORD');
 
    await api.processWorkouts({}, (workout) => {
        console.log(workout.toString());
	//console.log(workout.typeId);
	if(workout.typeId == 2) {
        //if (workout.hasGPSData()) {
            fs.writeFileSync(`tmp/${workout.getId()}.gpx`, workout.toGpx(), 'utf8');
        }
    });
})();
