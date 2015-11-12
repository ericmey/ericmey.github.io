import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import { spawn } from 'child_process';

const plugins = gulpLoadPlugins();

gulp.task('default', ['run']);

gulp.task('build', (cb) => {
  spawn('jekyll', ['build'], { stdio: 'inherit' }).on('close', cb);
});

gulp.task('run', (cb) => {
  spawn('jekyll', ['serve', '-w'], { stdio: 'inherit' }).on('close', cb);
});
