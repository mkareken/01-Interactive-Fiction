{
  "passages": [
    {
      "text": "You are in a white room with no doors and no windows. There is a red button on the ground in front of you.\n\n[[Press the Button->You Pressed the Button]]\n[[Do nothing->Nothing is happening]]\n[[Try to leave->You can't leave]]\n[[Go West->Which way is west?]]",
      "links": [
        {
          "name": "Press the Button",
          "link": "You Pressed the Button",
          "pid": "2"
        },
        {
          "name": "Do nothing",
          "link": "Nothing is happening",
          "pid": "3"
        },
        {
          "name": "Try to leave",
          "link": "You can't leave",
          "pid": "4"
        },
        {
          "name": "Go West",
          "link": "Which way is west?",
          "pid": "5"
        }
      ],
      "name": "The Button",
      "pid": "1",
      "position": {
        "x": "405",
        "y": "169.5"
      }
    },
    {
      "text": "The room goes dark. You can't see anything.\n\n[[Press the button agian->You can't find the button]]\n[[Do nothing->Dark nothingness]]\n",
      "links": [
        {
          "name": "Press the button agian",
          "link": "You can't find the button",
          "pid": "6"
        },
        {
          "name": "Do nothing",
          "link": "Dark nothingness",
          "pid": "7"
        }
      ],
      "name": "You Pressed the Button",
      "pid": "2",
      "position": {
        "x": "178",
        "y": "320.5"
      }
    },
    {
      "text": "You wait. Nothing seems to have changed.\n\n[[Continue to wait->Still nothing is happening]]\n[[Press the button->You Pressed the Button]]",
      "links": [
        {
          "name": "Continue to wait",
          "link": "Still nothing is happening",
          "pid": "8"
        },
        {
          "name": "Press the button",
          "link": "You Pressed the Button",
          "pid": "2"
        }
      ],
      "name": "Nothing is happening",
      "pid": "3",
      "position": {
        "x": "328",
        "y": "320.5"
      }
    },
    {
      "text": "I said there are no doors or windows. You cannot leave.\n\n[[Press the button->You Pressed the Button]] \n[[Leave anyway->Bye]]\n[[Who are you?->Who am I?]]\n",
      "links": [
        {
          "name": "Press the button",
          "link": "You Pressed the Button",
          "pid": "2"
        },
        {
          "name": "Leave anyway",
          "link": "Bye",
          "pid": "19"
        },
        {
          "name": "Who are you?",
          "link": "Who am I?",
          "pid": "20"
        }
      ],
      "name": "You can't leave",
      "pid": "4",
      "position": {
        "x": "478",
        "y": "320.5"
      }
    },
    {
      "text": "I don't know. Use a compass.\n\n[[Check your compass->Wait a minute]]",
      "links": [
        {
          "name": "Check your compass",
          "link": "Wait a minute",
          "pid": "26"
        }
      ],
      "name": "Which way is west?",
      "pid": "5",
      "position": {
        "x": "628",
        "y": "320.5"
      }
    },
    {
      "text": "You spend hours crawling around trying to find the button. It seems it has vanished.\n\n\n[[Scream into the abyss->Wasted efforts]]\n[[Accept your fate->Give in]]",
      "links": [
        {
          "name": "Scream into the abyss",
          "link": "Wasted efforts",
          "pid": "17"
        },
        {
          "name": "Accept your fate",
          "link": "Give in",
          "pid": "18"
        }
      ],
      "name": "You can't find the button",
      "pid": "6",
      "position": {
        "x": "103",
        "y": "470.5"
      }
    },
    {
      "text": "You hear nothing, see nothing, and smell nothing. Time seems to halter.\n\n[[Give in->Give in]]",
      "links": [
        {
          "name": "Give in",
          "link": "Give in",
          "pid": "18"
        }
      ],
      "name": "Dark nothingness",
      "pid": "7",
      "position": {
        "x": "253",
        "y": "470.5"
      }
    },
    {
      "text": "You wait. Again, nothing seems to have changed.\n\n[[Continue to wait->This is boring]]\n[[Press the button->You Pressed the Button]]",
      "links": [
        {
          "name": "Continue to wait",
          "link": "This is boring",
          "pid": "9"
        },
        {
          "name": "Press the button",
          "link": "You Pressed the Button",
          "pid": "2"
        }
      ],
      "name": "Still nothing is happening",
      "pid": "8",
      "position": {
        "x": "371",
        "y": "475.5"
      }
    },
    {
      "text": "You wait. Still Nothing seems to have changed.\n\n[[Continue to wait->Is this fun for you?]]\n[[Press the button->You Pressed the Button]]",
      "links": [
        {
          "name": "Continue to wait",
          "link": "Is this fun for you?",
          "pid": "10"
        },
        {
          "name": "Press the button",
          "link": "You Pressed the Button",
          "pid": "2"
        }
      ],
      "name": "This is boring",
      "pid": "9",
      "position": {
        "x": "373",
        "y": "620.5"
      }
    },
    {
      "text": "You wait. Nothing seems to have changed. Please do something. \n\n[[Continue to wait->Achieve patience]]\n[[Press the button->You Pressed the Button]]",
      "links": [
        {
          "name": "Continue to wait",
          "link": "Achieve patience",
          "pid": "11"
        },
        {
          "name": "Press the button",
          "link": "You Pressed the Button",
          "pid": "2"
        }
      ],
      "name": "Is this fun for you?",
      "pid": "10",
      "position": {
        "x": "375",
        "y": "771.5"
      }
    },
    {
      "text": "You are inhibited by nothing. Your mind is empty. Your path is clear.\n\n\n[[Meditate->Meditation]]",
      "links": [
        {
          "name": "Meditate",
          "link": "Meditation",
          "pid": "12"
        }
      ],
      "name": "Achieve patience",
      "pid": "11",
      "position": {
        "x": "373",
        "y": "920.5"
      }
    },
    {
      "text": "You can feel yourself becoming one with the room.\n\n\n[[Ascend->Become enlightened]]",
      "links": [
        {
          "name": "Ascend",
          "link": "Become enlightened",
          "pid": "13"
        }
      ],
      "name": "Meditation",
      "pid": "12",
      "position": {
        "x": "373",
        "y": "1070.5"
      }
    },
    {
      "text": "All is one and one is all\n\n[[Transcend this mortal coil->Transcendance ]]",
      "links": [
        {
          "name": "Transcend this mortal coil",
          "link": "Transcendance ",
          "pid": "14"
        }
      ],
      "name": "Become enlightened",
      "pid": "13",
      "position": {
        "x": "373",
        "y": "1220.5"
      }
    },
    {
      "text": "Your metamorphasis begins. The form you are promised is great but your transition shall be agonizing.\n\n[[Begin->Pure Agony]]",
      "links": [
        {
          "name": "Begin",
          "link": "Pure Agony",
          "pid": "15"
        }
      ],
      "name": "Transcendance ",
      "pid": "14",
      "position": {
        "x": "373",
        "y": "1370.5"
      }
    },
    {
      "text": "Ą̶̧̡̧̜̮̣̗̗͎̖͚̭̮͖̰̎̆̊̆̍̾́̽͝͠Ą̵͖̟̺̭̲́̎͗̅̀̇͐̚͠͝Á̸̛̻͕͚̘̫͍͎̯͚̖͋͑͊͌̈́̈̆̍̊̐̚͘̕͝ͅĄ̸̰̚Ȃ̵̡̢͖͖̮̝̪̔͒͋̍́͋̍͘A̷̤̬͎͉͉̅̇́͝Ả̸̡̙̠͕̪͔̖͖̟͉̭̙͕̤̥̮̰͐̄͗̾̎Å̵͓̽͒̄̏̅͐͐͝͝͝͠A̷̛̗̩̋̔̉͆̍̏̐̇͊̊̈́́A̷̯̭̦̝͓̬̜̲̬̿͂͛͒̿̓̐̽͂͐̿̉̽͘͘͠À̷̳̞̰̤̠̀̅͌̔́À̶̙̭̯A̷̢̨̢̛̘̭̩̫̜̦̼̬̟͖̿̊̓̂̒̐̆̓͋̒̓͑͜ͅA̴͕̹̗͐̔͝A̸̘̍͝A̴̛͉͕̰̫̾̏̆̈́͂̇̀͒̒̄̌̋͊́͒A̴̡̬͙̺̪̝̙̰̻͕͙͎̋̐̀̊̈́̚ͅÀ̷̡̺̞̯͙͈̫̻͉̻̒̀̒̂́̀̅̆̿͊͆̀Ą̸̭̟̈́̊́͐͋̉̽́̇̀̋̀̕͘͝͝Ą̶͉̮̗̘͚͇̮̫̥̗͍͓͈̭̹̓͌͑͗̕͘͜͝Ą̸̛̖̠̳̪͖͎̖͖͇́̀̏̑̿͊̍̄̀͐̕ͅA̷̫̱̋̿̋̔́̿̔͗͌̃̿A̶̲̣̼̻̜͛̓́A̴̡̡̧̛͍̜͇̱̮̘̩̗̫̝̫͎̞͚͛̀̅̏̃͂̊̉͆͋̚̕̚͝Ȃ̴̘̼̣̲̣̣̜̮̏̓̿̊͆̆̕͜Ã̴̲͇̖̫̞͐ͅA̷͕͖̻̥̩̚A̵̖̽͐̈́̀̈́̑͝͝A̷̜̦̣̥̹͔͎̬̮͌̿̀̈́̓̍̂̈́̈́̔͛̀̇̏͘̕͜͝ͅA̸̡̨͖͓̱͈̺̫̖̯͚̻̳͛A̶̢͈̥̹͉̹͖̓̿̍̊̓͜͝À̸̡̧̹̰̣͎͍̣͍̹̭̣̥͚̪Ą̵͍̮̰̖̮͍̼̫͙̙͍̩͑́̃͋̈́̐̎̍̅͝͝ ̵̡̡̬̳̠̣͍͔̼̺̥͙̘̗̿̑̚͝N̷͍̎̂͒̽̔͒̂̀͠͠Ơ̶̞͓͕̪̈̓̍̃̄̾̒̒͜Ò̶̧͓͎͓̪̫̠̠̳̻̪̜̝̼͙̀̑̇͒̀͛Ǫ̴̹̫̮̘͔̞͕͕͚͇͚̮͑͑̉̽͂̚Ǫ̶̨̧̨̮̗͔͎͔̗͍̙̅͂́̔͊͘͜O̶̢̡͎̺̞͖̳̫̩̘̞͎̗͖̺͆̄̎̔̊̅̒̉̓̂̄͝ͅO̷̺̔͑̾́̃̐́́̃̇̏̇̚͠Ơ̸̭̰̣̰̤̦̱̠̓̎͒̑̀̈́́̿̒̾̓̚̚Ǒ̸̞̱͖̗͚̓̽͐̑͛̈́͘͝͝O̵̧̧̻͈̼͕̝̬̠̎͂͠O̸̢͈̲̝͖̺͓̥͙͖̝̒͋̒̕Ò̵̯͙̜̍̄̄̄͊̀̔̍͒̽̄́̚̚͝͝Ǫ̵̛̜̹̻̱͇̮͙̺̠͇͚̬̼̒̍͐̈́̿̉̔͛̈̂̆͝͝ͅƠ̸̮͙̻̬̤̭̊̓̊͑̆̉͋̀̈́̈̓͐̐̕̚̚Ơ̶̢̺͔̳͕̯̣̗͈̺͙̣̑̓̆̉̋̓̅̑̌̋̋͂́͘͝O̶̢͇̤͙̰͎͔̩͈̭̥̜̪̟̝̰̥͗͘O̶̧͖̠̣̪̤̥̻̞̰̝͍̥̭̦̅Ǫ̵̧̡̛̭̮̯͉̼̲̘̥̻̅̾̉͐Ó̷̩͎̉͐́͒̓̈̇͊̓̇̚̚͘Ǫ̶̠̮̤̫̥̰͉͙̰̹́̈́̽͜͠Ơ̷̡̢̨̨͙̤̥͙̩͖̫͈̺̂̀͛́͛̎̉̎̀̚͘͝ͅǪ̸̣̱̯͔̊͐́̃̈́̕͠Ơ̸̧̢̨̹̝̮̳̠̮̦̳̣̈́͐͛̽̀̈́͋̆̔̏̚̚͘͜͠͠O̴̢̢̭̗̗̳̮̞̔̈͌̿͘̕ͅȎ̵̡̟̖̙̰̑̆͆̄͐̐̿́̀̊Ơ̵͎͕̐̌͊̓̊͋̂͑̕͘͝͝Ö̵̡̗̖̠͎̫͉̺́̅͋̉͊͊̀̎̽̌̋̓͐̔̽O̷̮̫̟̓͗̓̏̐̍̌̑̏̄̔͘͝ ̴̝͓͒͋F̸̳͔̈́Ŏ̵̪̔͆̐̏́̂̿͗̈́͘͝͝R̷̡̠̟̦̤̹̥̪͕̠̤̗̅̓͛͝Ĝ̸̰͖̠̳̖̲͛̐ͅͅĮ̶̢̭͖͎̙̘͇͂̋̑̌̈̎̍̋̈́̇̆̒͆̋V̵̝̍̽̂͌̏͌̓̇͑̀̅̕̕͘͝Ȩ̴̥̤͙̰͎͛̒̍͋͆̆̏̇̌̀̓͆ ̶̢̢̧̮͔̣̖͕͓̭̬͚̜͋̄͗̎͠M̶̦̹̻̮̜̺͓̙̏̋͊̈́̽̆̽̚ͅͅÈ̵͙̮̳̰̗͇͓̝͈͍͋͛̈́̈̐̕ ̷̱̯̤̻̰͐̑̇͐̀F̵̢͕̹̺̖̤̻͚̭̈́̏͊̈̾͒͊̀̽̊̇̔́Ǎ̴̮̘͉̗̖͓̽̌̿̈̆̌̚̚͠T̷̨̡̪͕̣͔̬̳̏Ḩ̶̢̞͎̂̽̎̌͊̊͒͘E̸̛̞̝͇̍̎̔̈́́̄̄̉̾͐̆̉̂̒̕͝Ṙ̸̢̯̮͕̖̻͓͕̪̭͍̌̄́̀̋̕ ̶̯̐̈́̀́͐̈͠F̶̲̩̻̖̬̏͋̎́̅̀͗̎̆͆̔͠͝ͅÔ̸̙͉͑̈́̓͛̅͠R̸̖̖̪̞̮͇̩͖̫͕̼͎͚̝̭̲͈͛̎̀̾̽̈́́̄͠͝ ̴̡̛̈́́̅̇́̈͗̑̚̕͘͝M̴̡̧̧̧̖͓͙̗̳͙̭̼̲̥͎̭͎̌͑̐̇̅͊̒͐̍̅̒͘͝͝Ỳ̵̡̠͓͖͙͉̠̘̥̀̀͑ͅ ̴̛̺̟͔̗͚̲̤̤̖̬͖̞͎̈́̍̃̈́͋̂̿̈͐̈́̚ͅŞ̷̛̛̛̝͓̰̘̙̬́̉͊̾̇̂̈́͑͗̐́͛͠ͅȊ̷̟̦͎͖̠̠̮͑̍͒͗̐͂̃̚͜N̶͖̗̭͇̙͇̯͈̈͒͂͆̓̈́̅̏̿́͜͝S̶̨̺̦̲͓̹͕̰͌́͆̃̋̄́̉̕͝ ̸̯̙̮̰̺̅͛̋̓͐̍͗̈̂̽͛̌̀̕ ̷̧̨̲̟͖̫̻̎͗̓̆̑̑̆Ė̵̡̛̯̳̟͙͚̳̩̱̳̗̖͕͍̀̌͑́͂̅͌̔͆̈́́͘͝S̴̞͖̥̜̘͈̐̉̅̐͂̂̍͂͒̈́̈́̅̒̚͘ͅJ̷̼͙̯̲͙̘̟̦̣͙̟̲̈́̉̄͐̈́̊̂͋͜͠F̶̨̞̜̖̙̝͕̱̬̹̬̥̦͙̱͈̓͗̿͊͆̔̂͌̿̈́̑̚͝͝Ŗ̵̣̖̞͕̮̓̈͜͜ͅ*̵̨͎̫̍͂̚͝(̴̢͎̍͆͐͌̊̐̅̇̄̈́͑͠W̵̛̩͈͍͙̲͈̘͎͚͒̀̍̊̍͛̆̓̍̄̉̕͜͠͝͝ͅY̵͍̹̗̅̈́̑̎̈́̃́͗̈̂̀̏͑́͘̕#̶̢̢̢̧̼͉̜̦̬͇̺̬͙̦͛̄R̵̢̡̪̙̬̞̠̤͉͈̩͌̒͊́͜$̵̺͙͎͎̻̤̟͔̏́͊͠(̷̧̡̨̝̗̖͓̪̥͖̺̬̽̍̌͌͌̑̔̽̅̾Q̷̢̹̖͍̗͇̫̟͎͇͇̯̪̼̽̉́͋͂͛̋̅̀̀͝͝*̸̲̤̦̩̱̫͓̥̤͂̈́̆̐̕@̴͈̩̫̟̲̳̫͉̜̌̋́#̸̨͉͔̰̖͈̱̬̤͐̌̈̈́́͌̿͌̊̍̃̓̈́͒͝͠W̷̧̯̳̻͈̪͍͕̳̲̘̎͒͑̑̚4̸̛̹̪̐̓̈́͗̈́͋͒̄͋̾̚͝ͅȓ̴̢̨̳͔̬͎̘͈̩̘̩̪͍͙̟̽́́̇̑̌͜r̷̗̯͈̫̖̠̎̉̔͂̾͊͛͋ệ̸̩̯̼̦̙̀̎̚ ̶̨̝̲͖̙̝̰̠̫̺̺̞̳̃̌̍̀̀̀̑͊̾̎͊͘͜͠n̵̡̯̻̝͖͎̬̩̖͇͂̍̀̔͒̓̎͑͑̋͑͋͌̕̕͘͜͝w̶̨͈̠̩͉͚̳̭̖͖̪̝̬̬̭͐̾͑̊̈́͗́̌̚͜ȃ̸̧̡̺͚̦͈̥̹̱̯͚̳̤̗̓̍̽̆͋͆̔͋͗͗̾̚͠8̵̢̢̨̹̲̜̟͊͊̿ͅŗ̸͑̔́́́̔͌͊̈̄́͘͝9̷̨̢̘͉̙̣̬̦͇̟͇͔̪́̄̒̒̎͝3̷͓̙̼͕͓͔̪͕̫̖̪̪̈̌͜ͅu̴̥̩̯͉̯̜̲̟̺̮͚̺̠͉͂̀͋̀͘ẖ̵̖̫͖̫̬̜͉̹̖̩̩̞̏̾̑̑͐̐̚͜͝͝2̸͉̪̜̤̺̝͚͓̭̦̈̔͒̆̅̈̊̿̑̓̒͑̃̽̿̄w̴̨̨̛͎̦̲̭͍̤̫̣̫̻͉̮͕̩͂̋͒͐͂̆́̌̇͆̉̔̽̕͝͠8̴͓͎͖̭͍̺͘͜ư̴̘̩̥̳̰͎̗̻̱̭̩̣̻̘̺̽̂̂͌̐͐͋̌̚ḭ̷̻̑̊̇̽̎͗̽̈̑͘͝r̶̗͎̳̼̭̩̱̯͆͆̀͂͝͠ḩ̸̮̰̺͇̲̲̆͂̾͆j̵͎͂n̸̳̝̦̻͕͔̆̎̀8̶͖̤͚̞̊͐̋͆̕͝A̴̢̨͚̱̪̩̰̱̭̺̝̩̱̤̜͑́̎̆̀̎̃͒̈̊̉̔ͅ9̵̛̝̰̱̯̹͎̫̫̱͙͓̺̹̳̏̂̍̍Y̷͙̲͖̅̀̃͑̄̓̀̓͊͠ͅU̴̻͖͒4̸͍̬͓͉̭͛͂̍̑͊̋͛̍̀̎̍̂̕̚͜͠Ȩ̶̜̙̲̱̅9̶̡̛͖͇̘̘̪͓̱̺͉͖̫̍̽͌́͂̄̌̆͑͊͝ͅ8̷̢̛͈̅̎͋̂̽̏I̸̺̙̯̭̝̞̗̻̘̭͍͓͛H̸̛̛͓̼̅͛̊́̂̅̆̐̈́̑̾̊̚͘͠ ̸̜̙̜̜̪̹̻̥͓̈́̿̈́̽͂̆͂̓̃́̿̅́̇̐̕̚ͅͅa̶̻̱͙̥̫̐̌͋̽̈͝a̴̧̟̹̺̪̭̲̘̺̿̀̈́̾͆̑̏̈́̄̄̃͆̿̕͝à̸̧̛̘̯̺̥͕̞̞͖̫͚̲͎̆͐͋̀̅͊̋̈́̀̏̍̓̕̕ā̴̡͖̮̠͎͔̺̦̝̱̭̘͉͙̳̰̞́̾́̎͒̀̓͐̀̃ą̵̛̜̟̲͙̭̪͔̥͍̙̅͗a̴̧̨̨̮͎̠̹̖̝̮͈̟̫̞͎̋̀̈́̀͐̂͗̀̓̆́̑̚ͅa̴͇͍̳͗͋͋͐́å̶̜̪̺̮̻̥̇̃͌͊̔̌́͠͝ͅa̵̰̗̟̼̯̭̱̞̋͒̄͆̓̎̽̈́̆͒̎̿̀̑͘ą̴͍́́̎͐̏̈́̂͋̈́̀̄͘̕͝Å̴̡̼̮̩̺̹̹͇̫̯̼̙̤̼̫͕̽̌̋̿̿̏͘Â̴̢̻͇͔͉̬͔͇̬͚̼͇̠̆̋̇͑̐͆̇̇͐̇̕̕͝Ȃ̷̭͔̦̙̖͓̩̃̿̀̌́̏͆̐͛̎̍͋ͅͅÀ̵̛͈̣̭̓̔̒̃̿̈̊A̷̛̠͓̱̲̭͚̲̒͑́̾̈̈̒̀̔͆̚̚͝Ą̸͈̼̥͍̓́͋̔͛̐͋́̓Ă̵̡̛͖͚̥̱̱̔̓̐̉̆͑͌͌̀́͌̇̚͠Ą̶͇̣̠̤̫̖̼͕̥̞̩̘͓̤̉̆͊̈̇̀̎͘͘̚͝͝A̶͔͋̚Ą̴̧̯͙̼̦̆̽̋̓A̸͖̅̚A̶̧̭͒Â̷͓̯̪͓̘̣̤̹͇͙̻̏̒̓̉͛̓̿̒̈́͝͝͝Ą̴̧͈̟̝̞̟͖͚͖̯̺͈͂̏͋̌̍̅́̒̈́͜͠Ȁ̸̢̠̩͚͈̮̥͖̗͕̳̤̤̼̐͜À̶̢̡̢̤̫̥̥͉̭͉̞̱̙̱ͅ ̷̡̢̥͖̠̙̱̪͍̣͍͂͂̉͌ͅŖ̸͉̪̄̑̎̄̒̈́͆͋̈̒̀̀̑̏͠͝͝4̷̡͕͋̀̆͘͠Ȩ̷̝̙͔͍̜͖̤̻̙̜̝̹͔͉͓̭́̅̏̂̍̏̿̊͊̑̈́̀̈́̅͐͝͠H̴̞̟͇͈̮͖̹͕̖͚̱̥͓̰͙͆̌͊̈́̽̀̇̿̚͠͝Ạ̷̛̰̮̟̤͌̈́͑̆̈́͌̂̔͜͝W̸̛̳̺̲̪̭̑̿̋̐̊̓͊̾̐8̵̧̛̮̹̫̆̾̏̓̃̚͠ͅ9̶̧̡̝̙̣̮̗̝̗̮̗̣͕͚̈́́͂̾̓̿̅̒̎̕̕͘̚5̵̨͕̼̜̦͈͍̯̮̞͇̹͍̔̏͆̀͑͌̔̊̋͋̍̕͝͝R̶̀́̅ͅ4̷̧̛̘̥͙̥̪͍͎̭̦̀͆͑́́͛̐̓̈̊̚̕3̷̢̗͍̬̺̗͎̯̻̲̝̱̽̃̿̅̿͒U̶̯͉̇̏̀͆́̈́̀̓̉̑̆̅̈̐͘͝Ě̵̥͔́̓̈́̍̏́͝͠W̴̡̡̞͖̤͍̯̯͔̩̣͕̻̦͙͑̃̀͗̉̀͌̒ͅͅ ̵̳̥̭̙͍̹̞̭̪͕̰̻̥̼̜̈̿9̸̬̟̹̩̯̲̮̂͜Ų̸̧̛̫͙͓̙̰͉͔̩̠̹̂̂̇̈͊̋̂͌̾̓͂͘͝ ̵̢̢̨̡̤̖̖̫̜͍̖̺̥̱̩̉͒̀̐̽̄̈́̈́̂̉́͜T̶̡̡̧͍̣̬̯͍̣̪̯̮̱̐͂̏̽͜͠ͅͅH̶̨̧̧̟͍͔̜̗͖̙̯͎̟̮̥̲̝̀͌̈́͊͗͋́͠E̷͎̞̤̠͈̺͔͇͕̞̩͗̎̉͛̅͠͠ ̶̫̠̺̦̱̳͈͇̞̐͛̎̐̍P̷̡͔̗͖̟̹̰͒̇́̀͜A̸̧̳̱̫̥̺̺̹͉͎͔̬̦̦̓̄̀̾̎͌̕ͅͅI̸̭̙͚͍͙̔͆̊̈́͗̀̕̚͝ͅN̸̖͊̈̑̋̍̈́̚͝ ̶̧̨̰̫͍̮̗̳̫̟͍͖͗̄̒̌̈́̈́̌̕͝Ḯ̵̧̨̢̛̛̳̦̯̘͈͓͔̞̘̩͓̭̺̋͛̆̒̒̿̊̓́̍̈͝Ś̸̡͔̯͎̲̮̮̫͚̊̀̂̈́̊̐͊́̆͝͝ ̸̧̨̺͕͈̹̪̲͌̎͆͐̉͗̐̾̆̐̋̈̉̈́͘͝Ţ̷̛̼̰̮͔̼̠̯͉͔͎̝̯̗̾̒̾̍̍̔̈́͜Ở̵̧̩̠̞͈̜͎̜̅̄̓̃́́͛̐̍̄͋̋͘O̷̡̲͈͑͛̀́̐͋͒̉̇̔̉̿̃̕ͅ ̶̢̡͉̞̩̗̝̠͍̺̜̞̓͗̏̐̆͜G̸̦̝̮͉͎͚̻͚̺̖̞̻̾̈̆̓͘͝R̵̜̪̞̄͂́̔̒̿̆̔͊̈́͆͑̒̕͠͠E̵͍̫̦̿̓̎̐̏̆̀̀̋͒̈́͌̍̾̔̚Ắ̸̛͖͉̺̙͈̝͓́̒͌̈́̾̓̾͋̎̀̋͘͘͜͝T̸̢̨̛̼̬̂͛̃͂͠ ̴̝̭́̒͗̓͒̓̐̀̓f̶̧̢̖̖̞͎͚̯͙̀ͅe̶͍͍̺̿͗̉̑̃͝i̵̝͚̝͚̗̪̐̌͋̉͐̉̀̄̐͝͝j̸̤̪̼̼͈̤̺̐̅͑̇s̷̨͖̫̮̠͙͔̞̳̹̮̗̽̏̓́̂̏͜ȧ̸̟̗͕̲͐̂̿͝W̵̡͈̟͍͎̙̯̰͎̝̘̓̐͐͒̒́̏̓͆̚R̵̰͕̪͓̓̓̋̏͗͋̇͊̀̐̀͝O̸͙̩̝͙̝͚͐̉̏̀͑͊͆̎̿̂͠*̴̢͔̯͛́̆̈́͂̚͘͝(̷̨̧̨͚͓̘̞̰̰̻̪͇͍͉̼̝̍̈̀̏̂͘̚Y̸̡͉̬̘̹̏̽̍Ų̶̹̠͍̠͚̦͇̠̬̟͓͚̞̐̂̅̐͑̃#̴̡̳̳̭̺̗̥̹̜̌͒͛͆̄̈́̀́́͗̕͝͝͝ͅẀ̵̨̢̢͇̹̱͖̞̲̠͕͎̓̉*̴̨̢̜̦̬̮̜̤̺̗͖̳̹̖̦̪̐̃̒͆̽̐̔̅̀͊̐̃́̔̔͝͝Ṙ̷͖͈̑͒̅̂̾̽̋͒̊́͐̇Ḩ̵̘̦̭̪̦̭̝̗̠̜̞̋͐̌͛͛͆̎̉̅̈̇̈́͊̂͋͘#̸̫̠͖̺̖̭̯̈́̏*̶̪̇̀̆͋͗̉̋̈́̎̈́͂͗͆̚W̶̧̭̘̜̙̭̩̪̹͈̹͜͠Ẽ̶̢̳̥̳̥͙͚̺̜̺̯̮̼̆̇́̃͛͌̃̄̃͌̆͛̑̚͜ͅͅ ̴̧̤͕̩̖̊̂́̇͐̋̕̚͝͝J̷̨̣̖̬̻̌̀̿͑̂̈́̂͋̒̅͘̕͘͝Å̷̡̪̻̩̱͚̗̥͚̙͚̲̙̟ͅW̸̛̻̻̃̓̃̒̚͝Ḙ̷̭͉͇̩̦̥͓̋̂̈́̂̍̌̒̀̊͗Ṙ̵̡̡̢̗̭͎͔̠̫͓̭̪̖͖̜̑̉̃̄̅́̒͛̈́̔͜(̵̨̦̤̖̥͉̪̟̗̞̠͉̂*̵̛͎̺̣̣̯̥̹̓̀̾̓͂̀̄̄̽̔̕ͅ)̶̨̧͖͎̫̖̭̠̝̅͝P̷͇͊̿͗͌͌̒͗̐̒̚ͅ@̶̧̧͙̼͐̅̎͊̈́͌͗̒̕Q̸̘̭̭̣̙̮̱̀́͂̚͜͝ͅU̸̟̮̼̞̻̰̭̣̜̠͒̀̓̅͛̆̐͐̊̓͆͐̚͝ͅȨ̵͖̥̠͇̱̩̿̈͂́̽̏̓̐͒̎̈́̐̏̚̚͜͠͠ͅ ̸̨̙͖͔̞͇̲͖̯͈̺̘͙̱͇̞̪̽̔̎̔͆̉̎̀̇̓͝r̵̛͓̤̲̘̪̮̍̓̄̊͂͐̈̍͐̍̔͗̆̄̈́0̵̱̟̣̗͍̽̌͛̽̚͜ͅ9̴̧͉͓͉̫̦̞͓͇̩̪̖̉̄ͅȩ̵̨̥̱͚̺͙͎̰͙͖̙͐͐̄̀̆̇̂̍̄̎̽͊͆͘͠-̷̰̬̻̲̖̈́̀̉̽̈́̋͘ͅͅř̶̨̟̥̭̩̥̟̥̰̞͇̭̇͜ͅt̸̼̄̈́̎̎͛̾͝į̴̧̛̮̱̪̥̤̳̝̬̻̗̮͔͉̯͑́̑̈́̾́̇ͅu̸͖̜̫̱̍̍͂͋̓́͆͌̃̾̆͆̔̐̐̕͜͝w̸̛̱̳̙̲̍͐̍̐͗́̒͝3̷̢̛̜̖͙̞̖̟̠̲̙͉̥͚̺͎̠̎̈̊̌̉̈́̐̈́͘4̴̱̻̟̝͍̽̓̽̕%̸̰̤͙͍̣̠̼̭̞̪̟̦̔̀̑͋́̎̀́͑̿̃̄̏͐͘̚͝ͅ(̶̡̦̼̩̜̥̜̎͆͒̈́̾̉̏͊͜H̴̨͈̜̬̗̦̮͖̋̚ͅJ̸͚͓̦͇̳̫̍̚T̸̖͖̝̠̰͂͋̾͛̌̈́͌̈́̈́̐́͆̈́͘͝ ̸̢̹̻͋̉̿̈́̈̽̎̐͜Ả̶͚̺̈́Ḁ̴̡̤͇̙̬͇͕̻̅Ã̶̡̛̳̦̬̳Å̵̪̗̋̽̍̌̌A̷͍͓̼̦̩̗̬̩̭͂̾̃̐̅̈́̀̈́̊͠͝Ä̴̟͇̲̺̗̦̗̠̼̦̲̣̗̟̙̪́̀̽̿̐ͅẠ̸̢̡̼̜̣̺̜̘͙̜̬̅͐́̓͆̎͐̓͊͌̈́̾̇͛͝͝ͅA̶̛͚̅̋̈́̓̈́́̊͝Ą̶̢͍̼̲̼̬͙̺̈́̌̏̍̿̃̕̚̕Ą̶͇̩̜͔̠̭͙̔̾͜A̷̧̡̨̡̺̭͚̬̥̥̲͚̱̣̔A̵͙̫̽͜͝Ą̶̛͈͍̪̪̥̰͚̜̫͔̯͇̓̾͆̐̈̊͛͊̔̎̊͜͜͜͝͝A̴̛̲̫͇̍͛̿̏̿́̐́͠Â̵̰̦̭̹̦͉̣̪̻̳̯̯̌̓̒͑͐̔A̴̧̛̹̯͕͚͙̦͍̓̈̉̈́̈́̃͋̋̅̑̎̅̈́͑͘͘A̷̢͔̲͓̲̩̼̍̅̀̂̎̉͝A̸̧̧̢̞͚̞̱͓͖̺͑̍̎͂̀́̓̕͜͠A̷̘̯͎̯͎͈͈̬͈̅̎͐̃̉̚Ḁ̶̲̔̓̽̈́̒̀̊͂̈́͌̽͐͠A̷̮͓̖̲̮̻̰̫͇̜̒̎̑̉̇̎́̃̓̋̿͋̓͆͘͘͘ͅÃ̴̧̧̩̥̬͖̮̥̦̗͈͜A̶͍̹̩̪͔͚̰̋͋͂͛̈́̍̇̌͋̃̔͝A̸͖͎̦͕̖̬͇̠̼͌͗̃̈́̏̆͊̈́̈́̏̅̅̓̎͌̈́͝A̶̠͔̮͚͋̒́A̶̧̙͕̽́̉̚Ã̸̛̟̅̈́̑̐͘͠Ā̶̛̻͌́͊Ą̸̗̯̳͙̤̪̝͓̤͌̌̇́́̂͝Ȁ̸̗͓̅̀̂̏̏͋̄̍̓͛̚͘͜Á̷̡̨̢̺͚͈̥̝̤͎̞̯͕̙͈̥͠͝Ą̷̡̢͙͖͎̜̭̬̳̬͉̘̻͈̗̮̀͐̀̅͛͊̄̅͌̂͒͝Ä̷̝́̈́̌̃͒̓͌ͅA̸̛̙͔͕̺̻̻͖̜̟͙̦̟̗̿̏͗̓́̚ͅȀ̸̧̟̓A̴̢̡̢͚̺̮̘̭̩̰̍̔̃͑͒̆̂̆͐̈́̔̕͜Ặ̸̣̖̘̉̿̎̄̒̑̑̌͂̍͝Ǎ̴̡̢̲̯̠̘̭̝̟̺͉̞̖̝̘́́̄̇͂̽̒̇̑̅̏͜͜͝À̷̛̬̬̭̙̥̥͉̦̲̪̝̍͊͠͠Á̶̡͍͕͕͉͍̥̜͖͇́̇̔͆͐̀̓͜A̸̢̡̞̱̥̰̠̦̣͈̘̺̫̽͜Ä̵͙́̃͑ͅA̸̧̩̅̊͌̄̆̂̊͑̄̒̍̃͆̕͝͝͝A̶̧̧̻͓͖̬̬̹̲̩̦̤̹̱̗̬͓̓̀̐͆͛́͛͊̇Ą̴̻̭̞̗́̽̇͑Á̷̛̙̲̗̪̥̮̪̱̺͙̱͍̻̱͔̔̆̍̋͐̕͝ͅÀ̴̛̜͎̋̈̂̏̍̂͒̏̚͝͝Á̵̢̻̯̱̉̓́̐̆̈́́̈́̔̑̄͗͘͠Ǎ̴̡̘̰͉͚̳̲̞͖̳̰̖̜͉̼̌̈̿Ả̸̘̝̣̟̦̘̗̜̲̥̺͍̈́̍̈́̔̑̈́̚͘ͅÁ̷̡̦̣͍̪͎̦̈́̍̓̐͝͝Ã̸̧̟̠̙͕͑̍͂̏̊̉́͐͛̈́̇͝Ả̵̡̖̳̜̗̦͉̪̼̪̟̻̺̤̮̹̔͐̐͑̏̐̋̿̂̔͝A̷̛̛̮̟͐̃́̅́̍̇̓̓̚A̸̛͈̹̬͇͖̠̾͛̆̈̎͛̓̂̋͗̌̆͝Ă̸̧̡͙̼̞̣̰̬̮͓͎̰̫̝͕͌͂̃̅̒̊̀̓̏̓͘̕A̷̡̛̛̪̹̤̖̔͊͋̌̈͂́̀͒̔̿A̸̧̜̼̤̩͎͉̯̜̟̾͗̽́̔̽̕͜ͅA̷̛͈̱͓̦̣̍̒̒͂̂̍̿͐̄̎̄͝A̴̢̧̯͔̬̰̲̐A̴̛̲͐̑͛̄̀̑̒́̀̈́̊̚À̷̫̪͚̣̹̣̭̲̞̹̯͍͗̐̽̓̿͒̏͘͠ͅA̷̛͔̘̠̼̬̯̻̪̮̪͉̍̆̏̇͌̏̆͊̔̏̌̚͜͝͝Ă̸̖͓̫̺̼̦̓̋̏̈́͝A̴̤̖͓̼͚̪̓̎̔̓̚͜A̴̢̨̢̨͈̙̣̬̪͓͍͕̠͈͌́̐͂̅͑͠ͅA̵̢̨̧͕̲̟̰̦͓͙̹̹͓̭̭͎̅̓̉̾̃́̓̑̈͋̌̓͘͘̚͝͝A̶̳̩͉̯̗͓͔͔̹͓̰̋͋̆̌ͅĄ̴̻̯͔̻͕̰̰͎͙͈̯͖̣̥̞̣̏̇́͛̂̔̔͒̓̎̎͛̍A̸̫͉͌́̒̉̐̆̚̚À̵̯̭̪͙̫̰͓͉̲̹̿̐͒͘͝ͅA̷̢̧̧̛̱̹̤͎͓̭̰̙͚͊͑̂̉̾̅̽̿̈͆̚͠Ã̶̢̛̛̮͙̤̗̜͖͈̙͙̥̻̦̦̖͋͑̄̓̀̊̈́̊̕Ą̶̠̝̳̘͉̹̲͇͔̼̯̯̤̲̽̔̊̓̆̊̿̂̀A̷͎̞͂͗͆̈̽̈́̈́͛́̚͝ͅA̸͓̥̝͇̻̲͎̖̖̽̔͌͌͐͆͝͠͝Á̷̰͙̙̯̻̮͂̈́̌̒̉͐̕͘Ą̴̡̥̰̠͔͙͉̙̞͓̘̜̮̣͉̿ͅẤ̴̡̢̫̯̹͍͙̟͕͔̺̣̠̦͇̰̩̉͑̂̓͑͂͛̍́̇̍͗̆̚͝A̶̛̠͔͍̾́̂́̄͐̔̔̈́͌͘͠Ą̵̦̠͈͈̙̰̬̋̎͐̃̽́́͆̒̆͗͒͝͝A̴̬̪͈̠̣̜̝̗͒͛̒̋́̊̏̿͝À̵̠̹͈̫̑͋͐͒͜A̷̢̭̻̫̫̩̤̦̣̥̪͈͙̦͚͛͂͊̌̀̏̈́Ä̶̛͎̻̦̖̰͍̻́̂͗̀̓̈́̏͒͝ͅĄ̵̔̊̓̏Ḁ̸͚͔̣̟͔̣͎̓̇͠A̵̳͔̜͇̻̼̪̜̤̳͖͙̝̠͂̑͆̅̌̔̊͋̋͜͜Ā̴̤͈̼͈̽̊͐͂̃̅͝͝A̵̧̨̢̨̹̹͓̲̤̜͌̒̋͂͛̽̈̃Ḁ̷̯͕̱̳̣̬̚ͅA̵͇̫̪͍͕̟̖̬̮̟̹̤̕A̴̡̜̫͆̊̋̌̒̋̇̉̍͑̊͑̅̇͊͋͝A̷̛͉̺̣͓̙̟͔̯͌͑͒͌À̶͈̰̹̫̼̈́̓̾̔̔͗̀̔͋̐͛̐͑̀̚͝A̴͎̣͑̾̋͐͑̌̈́͊́͂̄͊͑͒̚͘͠ͅẠ̵̥̟͎̝̟̫̪̲̗̮͚̱̖̠̋͊̒͊̿̕Ą̵̗̲̝̉̓̂̊̒̋̈́̽͌͘A̵̧̦̯̙̳͙͉̠͓͎̓̄͠A̵̡͖̫̖̥͔̤̩̹̼̫̰̾͌̆̌͆̒̌͘͝A̶̢̩̬̮̰͇̞̮͎̫͋A̵̡̨̻͖͉͖͚͎̠̭̞͇̲͙͛̋̋̊̉̔̇͛A̴͈̞̪͙̘͙͗̍́͆̈̔̀͊̄̈̑̈́͌̚͜Á̵̛̙͉̭̙̥̮̹̚Ä̸̛̠̻̱̪́͆̊̈ͅͅA̸̜̩̼͒͂̿͆̿͒͋̑͜͝A̵̘̪̯̱̙̘͓̰̱̿̍̑̐̐̅̒͘͘͠͝Á̷̧̢̀͑̅̔̽͗̒͒A̸̛̞̔̈́̊͆̈́̍̍̒̓̓̅̆̓͆͝͝A̴̡̢̛̛̗͕̭͈̖͕͔̪̯̪̪̗̿̃̐̎̌͛̏͆̈́͂͝Ẽ̷̛̲̙̹̻̫̱̳̦̻̭̭̪̦͕̆̆̊͋͆͂̇͗͐̅̎̚͝͠R̸̡̢̡̛̮̟̘̟̯̯̰̝̿̍͋͠I̷͙̼̝͔̬̻͔͉̻̟̱͔̰̔͂̓̋̆̒͆̄̂̌͗͛̀́͋͜͝͠F̶̧̨͉̬̰̭̗̥̏̉͜Ử̴͍̝̘͈̈́͒̔͊͛̇̆̄͒̏́͆͘͘͝W̵̨͚̠̮̻̘̯̯̬̦͎̬̟̜̩̄̈̏͌ͅͅ(̶̨̙̾͌̑̕͝*̸̛̟̣̀̒̀͗͂̍͋)̸̡͍͉̳̫̪̣͇͔̣̓̆̒͌̅͂̓͜͜R̸̛̖̈#̸̨̧̝̳͖̙̹͎̙̻̙̎͛̈̆ ̷̨̨̢̫̯̟͔͇͉̳̲̮̭̖̟͛́E̶̜̪̟͈͓̘͇̭̪̗͈̫̣͂͐̌͛͂ͅF̸̤̦̀̀̃̚R̷̨̠̺̼͓͓̅̀̏͒͝(̷̛̳̩̘̆̀̅͌͂̑̅̃̚U̷̙̬̟̥̹̲͇͗̈́̂̊̉͆͆͂̽̚Ĵ̶̢̨̲̻̪̮̭̹̤̤̪̖͎̘̱͓͌͊̿͛́̓̉̒̊͒͑́̕͘͜Ḏ̵̊̆̍͐̃̽͒̽̂̓͌̓͠͝Ş̶͇̜͓̬̞̬͈͔̜̹̪͖̃̉̈̽͊̊̀͑́̍́̿̏͘͜͝M̶̡̞̜̘̜̤͊͘N̵̡̫̔̈́͒̃̂̐͆̔̔̆̀̚͝͠F̷̹͈̗̲͚̣̱̩͙̭̠̋̇̿̒̎̔̐̆̇̌̎̑̀̇̕͜L̵̗̞̯̮͕͖͈̱̯̫̼̈́J̷͎̻̹͇͇͈̝̤̦̲̼̯͌͆̿̊͠K̵̛̻̲͚̟̮͈̹̲̫͉͐̇̈́̈̊̍̀̇̒̀̓̾͒̀̕͝Ḑ̶̛̹̳̯̬͙̜̼͔̆̈́͂̅͂̊̊H̵̟̘̯͈͓̥̲͔̳͚̼̹̝̯̩͚͕͗̉̓̂̆͗̂͑́̀̈́͘F̵̪͒*̶̹͔̮͇͈̝̱̆͑͗͐̎́͛I̸̱̪̰̩̮̰̦̮̱̮̪͕̰͔̦̅͋̌̏͒͋̈́̔̍̋̅͑͘͜Ǫ̶̨̡̜̟͈̳̞̩͔͔͈̲̗̭̌͌̈́̚W̵̨̢̭̼͈͖̦̆̋͝$̴̛̘̉͌̃̃̈́̂͌͋̓͆̀͊͠͝#̴̨̧̥͖̥͓͎̬̣̫̟͋̌̍̾̒̇̈́͝E̸̮͂W̸̢̛̹̺̝̟̼͚̲͋̌̐͐͐̋̈́̐͗͠͠ ̸̛̮̤͇̩͔͕̖͈̤̫̬̻̣̝̪̂̋̏̊͋̽̾̃͛̾̈́̀͑͘R̸̨̠̺͒̈́̿̈́̏̌́̍̅̌́̑͘F̷̛̛͉̩̓̂͛̅͂̆̿͑͌̇̓̐̋̒ͅ(̶̮̩̖̎̒̀̋̌̎̌̆̄͆̀͝͝)̴̪̣̺͇̭̝͊̽̎̎̆͝ͅ$̷̧̨̗̤̰͎͚̈́̄̓͝Ŵ̷̢̧͉͕̫̊̉̐͝Ê̵͍͚̭̈̄̂̑Ȕ̸̼̲͙͖̭̞̦̮͔̥̂̂̾̅̃͊͜͝͝R̶̢̠͙͉̙̅J̷̨͓̪͛͌̓͐́̎̽̊̃F̷̨̗̺͉̬̞͔͖̲͉̹̫̾̈͐̕͜ͅͅ#̵̡̢̛̟̥̲͚͍̟̮̳̞̇̍̍͒͛̓͑̈́́̔̊͝͝͠Ẉ̷̢̨̡̺̠̫͓̳͇͙̰̱̦̻͑̓͋͒̂̀̍̍ͅI̶̱̫͍͚̱̗͍̖̘̟̳̥̝̲͚̲͒̿̐̀͛̚̕̕E̸̩͓̳̳̥̲̼͉͔̫̿̈́̐͠ͅḾ̸̛̖͋̊̈́$̶̢̡̯̣̪̬̺͎̗̤̙͗̇̂͗͑̔͋͆̓̇̉̾̃͒̚̚͝R̸̨͍͕̰̳̋͆̔̈́͂͠͠F̴̨̛̛̲̬̼̪͉̲̦̠͕́̀̄͋͌͛͂̕ͅ(̵̮̱͈͖͍͍̪̖̘͇̐̆̍̓̿̇̅͆̔͐̀̓͘)̴͉̠̜̭͙͔̀̽̓͐̓̒̊̏̄̚Ȩ̵̛͍̹̲͙͔͙̰͉͙̦̮̠̼̞̏̂̈̊̕ͅD̸͖̱̭̣̟̳̩̼̰͆̂͝*̸̢̡͖̲̻͇̏̀̒ͅS̶̢̛̮̼̮̝̩̼̃͐̎̋͒̏̓̇̽́̊̂̚͘͜J̴̡̢̘̰͕͓͈͚̝̤͉͉̰̌̍̃ͅF̷̰̜̪̻̘̩͖̻̻͒͋̇̓̕͝͝͠N̸̨̝̱̙͈̦͎̮̜͍̝̩̥̲͂̏͐͑̈́͌̐̈͠C̸̱̦͕͖̟̞̼̭̗͖͎͓̟͕̀̿́̌̂̒ ̵̛̝̠̭̘͎̉̓̐̌̉̈́̓̔̚͜͠E̷̡͈͍̣̣̳̙̪̙͂̒̍̔͊͊̓͛̆̊͂̅͘͝ͅḐ̷̰͍̯͓̫͕̟̑͆(̵͙̮̬̯̜̄̍̉̍̈́̄͊͜ͅS̷̢͔̬͈͔̩̥̬͒̂̈̊̀̇ͅ)̵̢̡̛̣̯͇̞͔̞̼̘̜͛͋́̊͗̄͐͆̅̒̔̑̾͜ͅU̵̪͚̗̙̒͘͝Ŗ̷̨̡̗̹͇̪̗̥̞̜͚͍̗̅͐̏͗͗̓̍̉͌͛̓̑̚̚͜Ţ̴̜͇̦̭̣̣̮̱͉̦̠͂͊̑̓̌̊͑̆̈́̌͘̚͝F̵̢̹͈̺̒̔͐̌̾͋̓̈́̊$̴̡͕̼͎̳̆Ę̷̫̹͔͇̐͐̒̕W̷̤͇̲̾̍̃͂̿̐͊̆̊̂̕P̷͇͖̜̺̒̏́̽̏̂̓͐̉̍͌̾͘͠)̷̰̠̭̲̲̩̥̹͕͓̬̱̱̜̫̥̦̄̑̐̍͛́͌͂͐̈́̕(̶̡͕͍͎̟͔̲̤̬͚̀̄ͅR̶̨̠̳̳̱̱̗͓̅͊Ú̵̢͉̲̗͎̖̍̄̇͌͂̋̌͐̑̚F̶̢̠̞̘̦̝͉̞̜͔̅̽̃̌̂̃͗͛͛͜͠J̷̧̡̩̼̱̜̤̠̗̐̄͒̓͒̏̎̓̈́̇̊̔̕̚͝W̷̼̪̙̜͕̟̘͔̳̠̩̬̞̗͊̌̋ͅȄ̵͉͉M̷̛̲̣̠̱̦̗̣͆̆̎͌̊̏̈́̈́̿̓͝ ̸̨͔̈͑͂̃̋̏̾́̀̅̚D\n\n\n[[Complete Metamorphasis->Congrats!]]",
      "links": [
        {
          "name": "Complete Metamorphasis",
          "link": "Congrats!",
          "pid": "16"
        }
      ],
      "name": "Pure Agony",
      "pid": "15",
      "position": {
        "x": "373",
        "y": "1520.5"
      }
    },
    {
      "text": "You are now a furry. \n\n\n\n\n[[Restart->The Button]] ",
      "links": [
        {
          "name": "Restart",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "Congrats!",
      "pid": "16",
      "position": {
        "x": "373",
        "y": "1670.5"
      }
    },
    {
      "text": "You scream your lungs out. Nobody hears you. Not even yourself.\n\n[[Accept your fate->Give in]]",
      "links": [
        {
          "name": "Accept your fate",
          "link": "Give in",
          "pid": "18"
        }
      ],
      "name": "Wasted efforts",
      "pid": "17",
      "position": {
        "x": "28",
        "y": "620.5"
      }
    },
    {
      "text": "You accept your fate. The darkness is now your eternal prison for which you will never escape.\n\n[[Restart->The Button]] ",
      "links": [
        {
          "name": "Restart",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "Give in",
      "pid": "18",
      "position": {
        "x": "178",
        "y": "620.5"
      }
    },
    {
      "text": "NO! You can't leave! I created this world!! I AM GOD!!!!\n\n\n[[Bye->Euphoria]]",
      "links": [
        {
          "name": "Bye",
          "link": "Euphoria",
          "pid": "21"
        }
      ],
      "name": "Bye",
      "pid": "19",
      "position": {
        "x": "493",
        "y": "470.5"
      }
    },
    {
      "text": "I am god. I created the very room you stand in. That button is also my creation.\n\n[[God doesn't exist->HEATHEN]]\n[[Worship the Lord->Pray]]",
      "links": [
        {
          "name": "God doesn't exist",
          "link": "HEATHEN",
          "pid": "31"
        },
        {
          "name": "Worship the Lord",
          "link": "Pray",
          "pid": "32"
        }
      ],
      "name": "Who am I?",
      "pid": "20",
      "position": {
        "x": "613",
        "y": "470.5"
      }
    },
    {
      "text": "You obey no rules. You have no master. Even god fears you now.\n\n[[Make a room with a red button in it->Work in progress]]",
      "links": [
        {
          "name": "Make a room with a red button in it",
          "link": "Work in progress",
          "pid": "22"
        }
      ],
      "name": "Euphoria",
      "pid": "21",
      "position": {
        "x": "493",
        "y": "620.5"
      }
    },
    {
      "text": "You create a white room with no doors or windows. You place a red button in the middle of it. \n\n[[Make the Button consume all light->How torcherous]]",
      "links": [
        {
          "name": "Make the Button consume all light",
          "link": "How torcherous",
          "pid": "23"
        }
      ],
      "name": "Work in progress",
      "pid": "22",
      "position": {
        "x": "493",
        "y": "770.5"
      }
    },
    {
      "text": "The button will now deplete all light if pressed. You want to test it out.\n\n[[Put Someone in the room->Let the game begin]]",
      "links": [
        {
          "name": "Put Someone in the room",
          "link": "Let the game begin",
          "pid": "24"
        }
      ],
      "name": "How torcherous",
      "pid": "23",
      "position": {
        "x": "482",
        "y": "921.5"
      }
    },
    {
      "text": "You created a person and put them in the room. This person doesnt seem to be conscious. You need to add a soul to it.\n\n[[Soul binding technique->YOU FOOL]]",
      "links": [
        {
          "name": "Soul binding technique",
          "link": "YOU FOOL",
          "pid": "25"
        }
      ],
      "name": "Let the game begin",
      "pid": "24",
      "position": {
        "x": "482",
        "y": "1071.5"
      }
    },
    {
      "text": "YOU BINDED YOUR OWN SOUL TO THE BODY. YOU ARE NOW IN THE VERY ROOM YOU CREATED.\n\n[[NOOOOOOOO->The Button]] ",
      "links": [
        {
          "name": "NOOOOOOOO",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "YOU FOOL",
      "pid": "25",
      "position": {
        "x": "482",
        "y": "1221.5"
      }
    },
    {
      "text": "You check your compass, and apparently you are facing left. However, something seems off. \n\n[[Head west->You run into a wall]]\n[[Shake the compass->Adjusted Location]]",
      "links": [
        {
          "name": "Head west",
          "link": "You run into a wall",
          "pid": "27"
        },
        {
          "name": "Shake the compass",
          "link": "Adjusted Location",
          "pid": "28"
        }
      ],
      "name": "Wait a minute",
      "pid": "26",
      "position": {
        "x": "733",
        "y": "470.5"
      }
    },
    {
      "text": "Dumbass.\n\n[[Shake the compass->Adjusted Location]] ",
      "links": [
        {
          "name": "Shake the compass",
          "link": "Adjusted Location",
          "pid": "28"
        }
      ],
      "name": "You run into a wall",
      "pid": "27",
      "position": {
        "x": "951",
        "y": "479.5"
      }
    },
    {
      "text": "The compass realigns. You see that west is actually directly behind you.\n\n[[Turn around->You turn around]]",
      "links": [
        {
          "name": "Turn around",
          "link": "You turn around",
          "pid": "29"
        }
      ],
      "name": "Adjusted Location",
      "pid": "28",
      "position": {
        "x": "853",
        "y": "620.5"
      }
    },
    {
      "text": "Thousands of arms grapple you and pull you into the abyss. Resistance is futile.\n\n[[Give in->Give in]]\n[[No. I am built different.]]",
      "links": [
        {
          "name": "Give in",
          "link": "Give in",
          "pid": "18"
        },
        {
          "name": "No. I am built different.",
          "link": "No. I am built different.",
          "pid": "30"
        }
      ],
      "name": "You turn around",
      "pid": "29",
      "position": {
        "x": "854",
        "y": "769.5"
      }
    },
    {
      "text": "You are simply built different. You now win any and all of your twitter arguments.\n\n\n[[Restart->The Button]] ",
      "links": [
        {
          "name": "Restart",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "No. I am built different.",
      "pid": "30",
      "position": {
        "x": "848",
        "y": "918.5"
      }
    },
    {
      "text": "You are struck down in the face of the ultimate being. \n\n[[Restart->The Button]]",
      "links": [
        {
          "name": "Restart",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "HEATHEN",
      "pid": "31",
      "position": {
        "x": "613",
        "y": "620.5"
      }
    },
    {
      "text": "Fear not my son(or daughter), I am here now as I always have been before. You are safe.\n\n[[Ask god the purpose of human life->The Truth]]",
      "links": [
        {
          "name": "Ask god the purpose of human life",
          "link": "The Truth",
          "pid": "33"
        }
      ],
      "name": "Pray",
      "pid": "32",
      "position": {
        "x": "733",
        "y": "620.5"
      }
    },
    {
      "text": "Lol here take some DMT you'll find out soon enough.\n\n[[Trip BALLS->The elves]]",
      "links": [
        {
          "name": "Trip BALLS",
          "link": "The elves",
          "pid": "34"
        }
      ],
      "name": "The Truth",
      "pid": "33",
      "position": {
        "x": "733",
        "y": "770.5"
      }
    },
    {
      "text": "So many elves. Too many elves. You start to tweak.\n\n[[Listen to Pink Floyd->Vibe]]",
      "links": [
        {
          "name": "Listen to Pink Floyd",
          "link": "Vibe",
          "pid": "35"
        }
      ],
      "name": "The elves",
      "pid": "34",
      "position": {
        "x": "733",
        "y": "920.5"
      }
    },
    {
      "text": "Hell yeah. Now we're vibing. This is the true ending of the game, why?, because I said so. GG\n\n\n[[Restart->The Button]] ",
      "links": [
        {
          "name": "Restart",
          "link": "The Button",
          "pid": "1"
        }
      ],
      "name": "Vibe",
      "pid": "35",
      "position": {
        "x": "733",
        "y": "1070.5"
      }
    }
  ],
  "name": "The Button",
  "startnode": "1",
  "creator": "Twine",
  "creator-version": "2.3.9",
  "ifid": "EFF47BB0-DD38-40ED-B234-BA84EB50C6BB"
}