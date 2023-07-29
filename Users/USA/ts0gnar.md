| User         | Password                          | Level    | Status     | Name          |  
|--------------|-----------------------------------|----------|------------|---------------|    
| ts0gnar      | loreta192BoxAre23right21          | observer | Active     | Tern Sognar   | 

# ts0gnar:loreta192BoxAre23right21 

* user<br>
  Login: ts0gnar<br>
  Access level: observer<br>
  Name: Tern Sognar<br>
  Status: Active<br>

  Description:<br>
  DELETED<br>

  Notes:<br>
  DELETED<br>

* dir
  * users.table<br>
    ```
      --------------------------------------------------------------------------------------------------------------------
      USER                       PASSWORD                                     STATUS                  MODE
      --------------------------------------------------------------------------------------------------------------------
      rtoezje               redKL3245pfvkl3j4                              Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      vidbowbo93-5          Jje=2ksxkk2p;1                                 Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      obtmvgcp              ME3krfm234icmMI5O3xsd                          Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      rtdsvmvg              34fkmo3pfdomsjdfkl45mf;sdf                     Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      ibcNovw               ml34fpomce,po3ld4g5f                           Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      sd0fgto               loreta192BoxAre23right21                       Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      bwbokbkbo              WX7571A4GE6XPRDRMY5U                          Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      lvcqxtdsbo             XY3451B4HR5LV3RZ                              Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      ivovw                  jiwerfplihuhec                                Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      ctdsxutvd              oi34jbhfiko3mf                                Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      ividrjsu               gosyrn32jcxnj                                 Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      vidbowbo25-2           alterkl3nrfuimjHY##                           Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      ftocjxtax              alfgtetqmqrnftgrmbry                          Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      otaotaota              ji3fkoeol34fm3mfkiedfvk                       Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
      eztavxwpzm             DELETED                                       Deactivated                AEC
      --------------------------------------------------------------------------------------------------------------------
    ```


    ```
    Affine key was got by noticing old passwords and trying to match the encrypted password to the known user name.
    
    sd0fgto --Affine decode with A15 B19 --> ts0gnar
    rtoezje -> marzqiz
    vidbowbo93-5 -> observer93-5
    obtmvgcp -> readonly
      rtdsvmvg -> mastodon
      ibcNovw -> belKrov
    sd0fgto -> ts0gnar
      bwbokbkbo -> everpeper
      lvcqxtdsbo -> wolfcaster
      ivovw -> borov
      ctdsxutvd -> lastchaos
      ividrjsu -> bobsmith
      vidbowbo25-2 -> observer25-2
      ftocjxtax -> garlicaxc
      otaotaota -> raxraxrax
      eztavxwpzm -> zqaxocvyqd

    but if we ENcode instead of DEcode the last username with Affine we get
    eztavxwpzm -> bestwalker

    note: both [A:15, B:19] and [A:7, B:23] work for Affine, just [7, 23] has to be used the other way - Encrypt where you would be Decrypting with [15, 19] and Decrypt on the other places
    ```
    
    ```
    some of the passwords belong to accounts we already have:
      rtoezje -> marzqiz
      vidbowbo93-5 -> observer93-5
      obtmvgcp -> readonly
      sd0fgto -> ts0gnar

    These should all be active by their user data

    These known accounts were used to get the substitution alphabet:
    A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
    x e l s z g n u b i p w d k r y f m t a h o v c j q

    However this is now probably not needed anymore since the Affine cipher keys were cracked (by trying and checking).
      ----------------------------------------------------------------------------------------------------------------------------
      USER                       PASSWORD                                     STATUS                  MODE                  VALID
      ----------------------------------------------------------------------------------------------------------------------------
      marzqiz               redKL3245pfvkl3j4                              Active                     AEC                   Y
      ----------------------------------------------------------------------------------------------------------------------------
      observer93-5          Jje=2ksxkk2p;1                                 Active                     AEC                   Y
      ----------------------------------------------------------------------------------------------------------------------------
      readonly              ME3krfm234icmMI5O3xsd                          Active                     AEC                   Y
      ----------------------------------------------------------------------------------------------------------------------------
      mastodon              34fkmo3pfdomsjdfkl45mf;sdf                     Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      belKrov               ml34fpomce,po3ld4g5f                           Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      ts0gnar               loreta192BoxAre23right21                       Active                     AEC                   Y
      ----------------------------------------------------------------------------------------------------------------------------
      everpeper              WX7571A4GE6XPRDRMY5U                          Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      wolfcaster             XY3451B4HR5LV3RZ                              Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      borov                  jiwerfplihuhec                                Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      lastchaos              oi34jbhfiko3mf                                Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      bobsmith               gosyrn32jcxnj                                 Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      observer25-2           alterkl3nrfuimjHY##                           *                          AEC                   *
      ----------------------------------------------------------------------------------------------------------------------------
      garlicaxc              alfgtetqmqrnftgrmbry                          Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      raxraxrax              ji3fkoeol34fm3mfkiedfvk                       Deactivated                AEC                   N
      ----------------------------------------------------------------------------------------------------------------------------
      bestwalker             DELETED                                       *                          AEC                   *
      ----------------------------------------------------------------------------------------------------------------------------
      Y = Valid Credentials
      N = Invalid Credentials
      * = Account of Interest
    ```

* notes
  * note1 <br>
    Made a request to pull all the users in our regional branch, but something went wrong and it put all those who are currently "Active" and "Deactivated" in the same list. I need to find the root cause of the problem.
  * note2 <br>
    Looks like I found the problem. Turned out it’s the “5-3-2” – I'll try to fix it now.<br>
    ```
    5-3-2 --letters--> ECB
    ```
  * note3 <br>
    No, that wasn't it. It wasn't about that part at all. I'll keep looking for the problem.
  * note4 <br>
    Also, for some reason all the logins are encrypted 1-20-8-5-14-1. I lost the key somewhere. I'll have to pick A & B at random. There's only a million options. Although it's clear that A is with a minus.<br>
    ```
    1-20-8-5-14-1 --letters--> ATHENA

    maybe the A and B are?:
    A -> user -> vidbowbo25-2 -> observer25-2
    B -> pw
    ```
  * note5 <br>
    Wanted to mess around with story generators. My first attempt was a bust. But what can you do? I wanted to generate a story about bones laid out in a square and inscribed in flaming letter keys to the meaning of existence. But something went wrong. I'll have to write it myself.

    \*\*\*<br>
    My skeleton key to the door has been chiseled, and now rests in the palm of my hand. One step and the door will be open. On another side of the door I see a small pit. Nathan in my head said, “if you can survive the fall and you reach the bottom of the pit you can climb up.” Light and air exist between me and the hole. I ascend roughly 6 feet to the bottom and then another 12 to the top. Gasoline pours from a yellow flame. Hanging beneath the fire are two axes. Through the steel grate of the bunker doors I see that the runway has grown cold. <br>
    \*\*\*<br>
    ```
    First letter of each sentence from the story -> MOONLIGHT
    ```
