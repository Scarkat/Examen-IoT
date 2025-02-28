% --- Código para mostrar el promedio de los últimos 10 datos y generar alerta ---

% Lee los últimos 10 datos de temperatura de field1
data = thingSpeakRead(2856350, 'Fields', 1, 'NumPoints', 10);

% Muestra los últimos 10 datos en la consola
disp('Últimos 10 datos de temperatura:');
disp(data);

% Calcula el promedio de los últimos 10 datos
promedio_temp = mean(data);

% Muestra el promedio en la consola
fprintf('Promedio de temperatura: %.2f°C\n', promedio_temp);

% Verifica si alguno de los últimos 10 datos supera el umbral de 35°C
alerta = any(data > 35);

% Genera y muestra el mensaje de alerta si es necesario
if alerta
    mensaje = '¡Alerta! Temperatura mayor a 35°C detectada en los últimos 10 datos.';
    disp(mensaje);
    % thingSpeakWrite(YOUR_CHANNEL_ID, mensaje, 'Fields', 3); % Opcional: Enviar alerta a ThingSpeak en field3
else
    disp('Temperatura normal en los últimos 10 datos.');
end