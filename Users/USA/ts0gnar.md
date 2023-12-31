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



    The key used for encoding the usernames was acquired by conducting a known-plaintext attack using previously obtained passwords from the branch; after identifying that an Affine cipher should be used, we were able to decode all of the usernames after bruteforcing an initial working key:
    ```
      rtoezje       -> marzqiz
      vidbowbo93-5  -> observer93-5
      obtmvgcp      -> readonly
      rtdsvmvg      -> mastodon
      ibcNovw       -> belKrov
      sd0fgto       -> ts0gnar
      bwbokbkbo     -> everpeper
      lvcqxtdsbo    -> wolfcaster
      ivovw         -> borov
      ctdsxutvd     -> lastchaos
      ividrjsu      -> bobsmith
      vidbowbo25-2  -> observer25-2
      ftocjxtax     -> garlicaxc
      otaotaota     -> raxraxrax
      eztavxwpzm    -> zqaxocvyqd
    ```
    If we encode instead of decode the last username with Affine, we get:
      `eztavxwpzm   -> bestwalker`

    Please note: [A:-11, B:19], [A:15, B:19], and [A:7, B:23] are all valid keys for the cipher.

    The accounts we already have the passwords to can be seen in the textblock below:
     ```
      rtoezje       -> marzqiz
      vidbowbo93-5  -> observer93-5
      obtmvgcp      -> readonly
      sd0fgto       -> ts0gnar
     ```
    These should all be active by their user data and have had their status updated in the table below.

  ```
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
      wolfcaster             XY3451B4HR5LV3RZ                              *                          AEC                   N
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
    1-20-8-5-14-1 --A1Z26--> ATHENA historically points to the Affine cipher.

    [A:-11, B:19] was determined to be a valid key that allows us to decipher the usernames in the aforementioned `users.table` table.
    ```
  * note5 <br>
    Wanted to mess around with story generators. My first attempt was a bust. But what can you do? I wanted to generate a story about bones laid out in a square and inscribed in flaming letter keys to the meaning of existence. But something went wrong. I'll have to write it myself.

    \*\*\*<br>
    My skeleton key to the door has been chiseled, and now rests in the palm of my hand. One step and the door will be open. On another side of the door I see a small pit. Nathan in my head said, “if you can survive the fall and you reach the bottom of the pit you can climb up.” Light and air exist between me and the hole. I ascend roughly 6 feet to the bottom and then another 12 to the top. Gasoline pours from a yellow flame. Hanging beneath the fire are two axes. Through the steel grate of the bunker doors I see that the runway has grown cold. <br>
    \*\*\*<br>
    ```
    First letter of each sentence from the story -> MOONLIGHT
    Could possibly be a reference to wolves and imply that wolfcaster is the next username.
    ```

## garlicaxc
@Zephirim tried playfair cipher against all accounts with key `MONLIGHTABCDEFKPQRSUVWXYZ` (MOONLIGHT was derived from note5) which returned a cleartext password LYCANTHROPEXEATPIGSX; this needs to be converted to all lowercase to be useful for a password.<br> 
