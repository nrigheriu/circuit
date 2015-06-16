var gulp = require('gulp');
var less = require('gulp-less');
var concat = require('gulp-concat');
var path = require('path');

gulp.task('default', [
    'copy',
    'css',
    'js'
]);

gulp.task('css', function () {
    return gulp.src('./assets/less/app.less')
        .pipe(less())
        .pipe(gulp.dest('./circuit/static/css'));
});

gulp.task('js', function () {
    return gulp.src([
        './assets/vendor/jquery/dist/jquery.js',
        './assets/vendor/bootstrap/dist/js/bootstrap.js',
        './assets/vendor/bootstrap-material-design/dist/js/material.js',
        './assets/vendor/bootstrap-material-design/dist/js/ripples.js',
        './assets/js/app.js'
    ])
        .pipe(concat('app.js'))
        .pipe(gulp.dest('./circuit/static/js'))
});

gulp.task('copy', function () {
    return gulp.src('assets/vendor/bootstrap-material-design/fonts/*')
        .pipe(gulp.dest('./circuit/static/fonts'));
});
