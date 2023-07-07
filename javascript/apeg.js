window.addEventListener('message', function (e) {
  if (!/apeg\.cn/.test(e.origin)) return;

  const { command, data } = e.data;
  switch (command) {
    case 'txt2img':
      switch_to_txt2img();
      const txtInput = gradioApp().getElementById(`txt2img_prompt`).querySelector("textarea");
      txtInput.value = data.txt
      break;
  }
});