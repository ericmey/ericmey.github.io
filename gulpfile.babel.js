import gulp from 'gulp';
import gulpLoadPlugins from 'gulp-load-plugins';
import { spawn } from 'child_process';

const plugins = gulpLoadPlugins();

gulp.task('default', ['watch']);

gulp.task('build', ['build:includes', 'build:layouts'], (cb) => {
  spawn('jekyll', ['build'], { stdio: 'inherit' }).on('close', cb);
});

gulp.task('build:includes', () => {
  gulp.src(['_includes/jade/**/*.jade'])
  .pipe(plugins.jade({ pretty: true }))
  .pipe(gulp.dest('_includes'));
});

gulp.task('build:layouts', () => {
  gulp.src(['_layouts/jade/**/*.jade'])
  .pipe(plugins.jade({ pretty: true }))
  .pipe(gulp.dest('_layouts'));
});

gulp.task('run', ['watch'], (cb) => {
  spawn('jekyll', ['serve', '-w'], { stdio: 'inherit' }).on('close', cb);
});

gulp.task('watch', ['watch:includes', 'watch:layouts']);

gulp.task('watch:includes', () => {
  gulp.watch(['_includes/jade/**/*.jade'], ['build:includes']);
});

gulp.task('watch:layouts', () => {
  gulp.watch(['_layouts/jade/**/*.jade'], ['build:layouts']);
});
