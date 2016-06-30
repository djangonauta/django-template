var gulp = require('gulp');
var inject = require('gulp-inject');
var wiredep = require('wiredep');

var wiredepOptions = {
  bowerJson: require('./bower.json'),
  directory: '{{ project_name }}/static/vendor'
}

var js_files = [
  '{{ project_name }}/static/app/**/*.module.js',
  '{{ project_name }}/static/app/**/*.js'
]

var css_files = [
  '{{ project_name }}/static/css/**/*.css'
]

gulp.task('inject', function () {
  return gulp.src('{{ project_name }}/templates/base.html')
            .pipe(wiredep.stream(wiredepOptions))
            .pipe(inject(gulp.src(js_files)))
            .pipe(inject(gulp.src(css_files)))
            .pipe(gulp.dest('{{ project_name }}/templates/'));
});

gulp.task('inject-static', ['inject'], function () {
  var exec = require('child_process').exec;
  var command = './manage.py add_static_tags base.html --settings={{ project_name }}.settings.development';
  exec(command, function (err, stdout, stderr) {
    if (err) {
      throw err;
    }

    console.log(stdout);
    console.log(stderr);
  });
});