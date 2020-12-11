clear
m = mobiledev;
cam = camera(m,'back'); % 'front' なら正面のカメラを使う 

nnet = alexnet;

picture = snapshot(cam,'manual'); % 手動でシャッターを切る
picture = imresize(picture, [227, 227]); % alexnt が学習している画像の画素数
label = classify(nnet, picture);
image(picture);
% title(char(label));    % スマホだとラベルが小さすぎる
title(['\fontsize{40}' char(label)]); %`\fontsize{40}' を「書いて」、大きさを変更する
