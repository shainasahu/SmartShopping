// static/js/learn.js
document.addEventListener('DOMContentLoaded', function() {
    const startTime = new Date().getTime();
    const lessonId = window.location.pathname.split('/').pop();
    
    window.addEventListener('beforeunload', function() {
        const endTime = new Date().getTime();
        const timeSpent = (endTime - startTime) / 1000; // in seconds
        
        // Send the data to the server
        navigator.sendBeacon(`/track_learn_time?lesson_id=${lessonId}&time_spent=${timeSpent}`);
    });
});