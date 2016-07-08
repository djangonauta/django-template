const gulp = require('gulp');
const inject = require('gulp-inject');
const wiredep = require('wiredep');

const wiredepOptions = {
  bowerJson: require('./bower.json'),
  directory: '{{ project_name }}/static/vendor'
}

const js_files = [
  '{{ project_name }}/static/app/**/*.module.js',
  '{{ project_name }}/static/app/**/*.js'
]

const css_files = [
  '{{ project_name }}/static/css/**/*.css'
]

gulp.task('inject', () => {
  return gulp.src('{{ project_name }}/templates/base.html')
            .pipe(wiredep.stream(wiredepOptions))
            .pipe(inject(gulp.src(js_files)))
            .pipe(inject(gulp.src(css_files)))
            .pipe(gulp.dest('{{ project_name }}/templates/'));
});

gulp.task('inject-static', ['inject'], () => {
  const exec = require('child_process').exec;
  const command = './manage.py add_static_tags base.html --settings={{ project_name }}.settings.development';
  exec(command, (err, stdout, stderr) => {
    if (err) {
      throw err;
    }

    console.log(stdout);
    console.log(stderr);
  });
});
