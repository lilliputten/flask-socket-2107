/** @module sockets
 *  @since 2021.07.25, 22:02
 *  @changed 2021.07.25, 23:43
 */

$(function() {

  // const socket = io();
  // const socket = io.connect('http://localhost:5000');
  const socket = io({ query: { foo: 'bar' } });

  // const manager = new io.Manager({
  //   reconnectionDelayMax: 10000,
  //   query: { bar: 'my-value' },
  // });
  // const socket = manager.socket('/socket', {
  //   // auth: { token: '123' },
  //   query: { bar: 'my-value' },
  // });

  console.log('socket: initialze', socket.io, socket.connected, io.protocol, socket);
  // debugger;
  // setTimeout(() => {
  //   console.log('socket: initialze delayed', socket, socket.connected);
  //   debugger;
  // }, 5000);

  // socket.emit('my event', {data: 'Before Connected!'});

  socket.io.on('connect', function () {
    debugger;
    // $('#chat').addClass('connected');
    socket.emit('my event', {data: 'Client Connected!'});
  });

  socket.io.on('error', function (error) {
    console.error('socket: error', error);
    debugger;
  });

  socket.on('my response', function() {
    console.log('got my response', socket.id, socket.connected);
    debugger;
  });
  socket.on('my event', function() {
    console.log('got my event', socket.id, socket.connected);
    debugger;
  });

});
