A = (1.2e9 * 2 * 0.08) / (3e8);
B = (1.2e9 * 2 * 0.038095) / (3e8);

[mGrid, nGrid] = meshgrid(-4:0.01:4, -4:0.01:4);

F = sqrt((mGrid/A).^2 + (nGrid/B).^2);

figure;
[~, c] = contour(mGrid, nGrid, F, [1 1], 'g'); % Зеленый цвет для эллипса
c.LineWidth = 2;
axis equal;
grid on;
xlabel('m');
ylabel('n');
title('Эллипс'); % Заголовок на английском

xticks(-4:0.5:4); % Интервалы сетки 0.5 по оси X
yticks(-4:0.5:4); % Интервалы сетки 0.5 по оси Y

hold on;
plot([min(mGrid(:)), max(mGrid(:))], [0, 0], 'k', 'LineWidth', 1); % Ось X
plot([0, 0], [min(nGrid(:)), max(nGrid(:))], 'k', 'LineWidth', 1); % Ось Y
hold off;
