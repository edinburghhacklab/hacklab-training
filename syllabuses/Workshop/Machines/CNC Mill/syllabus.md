# CNC Mill

## Safety
### Awareness of risks
* Risks inherently associated with machining
 * Direct cutting risks (including from non-spinning tools!)
 * Hair, clothes, etc tangling in spindle/tool
 * Crush risks from moving axes
 * Flying chips
 * Parts flying on workholding failure
 * Sharp edges on stock, workpieces and chips
 * Hot tools and workpieces after cutting
* Additional risks of CNC machining
 * Unexpected movements
 * Crashes due to misplanned programs

### Use of safety measures
* Safety features of the machine
 * Emergency stop button
 * Protective cover
* Clothing and use of PPE
 * Safety goggles
 * Gloves
 * Ear protectors for noisy jobs
 * Aprons, boiler suits etc to protect clothing
 * No ties / scarves / jewellery / etc
 * Use of brushes to clear chips, deburring, etc

### Training

Start with a safety briefing - go through all the points above, in front of the machine.

Main hazards/risks should also be on warning signs / posters in the CNC area as a reminder.

During subsequent training, be ready to prompt if any safety measures or considerations seem to have been forgotten by the trainee.

### Evaluation

The trainee must be able to identify risks associated with the machine and the safety measures that should be used.

The trainee must be observed to routinely use safe working practices when working without prompting or reminding.

## Basics

### Turning on & startup
 * Switch on control box
 * Start up software
 * Release emergency stop switch

### Homing
 * What the homing buttons will do
 * When it’s safe to use each

### Feed & spindle override knobs
 * Be aware of sensitivity
 * Use gently

### Loading and unloading tools
 * Awareness of machine tool change cycle
 * Tools required & appropriate torque
 * Cleanliness of taper surfaces
 * Tapping with wood block to free tapers

### Setup and control of coolant system
### Cleaning machine area before and after use

### Training

Start by demonstration. Go through the process of turning on the machine and making it ready for use, talking the trainee through each step and the reasons for it.

Next, shut the machine down and ask them to repeat the process. They will probably need lots of prompting and help, this is fine.

The trainee will get further practice through routine use as they go through the training process. Be ready to prompt and remind as needed.

### Evaluation

The trainee must be able to set up the machine correctly without assistance or prompting, regardless of the state they find it in.

## Manual & MDI operation

### Jogging
 * Continuous mode
 * Step mode

### MDI
### Basic G-codes

### Training

First demonstrate jogging, with spindle off. Next, turn on spindle and show how simple machining can be accomplished at controlled feed/speed settings using the jog feature. Have the trainee try this to face off the top surface of some rough stock. Talk about feed, speed & depth of cut and encourage them to experiment with these, within safe margins.

Next, introduce CNC. Show how the same facing task can be done with G0 and G1 commands entered in MDI mode. Have the trainee complete the program and run it. Simple exercises like this will help them gain an understanding of what is being generated, when they move on to a CAM workflow. For very simple jobs it is also often quicker to write G-code by hand than to model a part and generate toolpaths.

### Evaluation

The trainee should be able to carry out simple machining tasks without use of CNC features, e.g. to face off all sides of a rough billet.

The trainee should be able to write G-code for simple designs, e.g. cutting a rectangle of given dimensions and drilling some holes at specified co-ordinates. They do not need to be able to remember commands and syntax - the use of G-code reference materials is fine.

## Workholding

### Understanding workholding requirements
### Use of workholding equipment:
#### T-nuts
#### Vice
#### Parallels
#### Step clamps
#### Toe clamps
#### Hex clamps
### Use of sacrificial material
### Clearance issues

### Training

There is no need to introduce all the workholding options at once; workholding should be introduced by example whilst working through the practice projects, eventually covering all the main techniques. The trainee should be made aware of the need for rigid workholding and the problems that can occur with an inadequate setup..

### Evaluation

The trainee must be able to choose an appropriate workholding solution for each job and set it up correctly.

## Offsets

### Theory of co-ordinate systems and offsets
### Squaring using a dial gauge
### Setting work offsets:
#### Bare tools
#### Slip blocks
#### Edge finder
#### Digital probe

### Training

The relationships between co-ordinate systems and offsets should be introduced with the help of visual aids and demonstrated by example. A visual reminder of the key relationships should be present in the CNC area.

Squaring should be demonstrated first, then the trainee should attempt it with assistance. Further practice will follow in the course of the training programme.

The different methods of setting work offsets should be introduced one at a time in the process of working through the sample projects. Again, these should be demonstrated first and then attempted by the trainee.

### Evaluation

The trainee must be able to, without prompting:

 * Explain the relationship between the different co-ordinate systems and offsets of the system.
 * Square a workpiece accurately using a dial gauge.
 * Set work offsets using each of the methods listed above.

## Tooling

### Use of tooling:
#### End mills
#### Ball mills
#### Chamfer mills
#### Spot drills
#### Drill bits
#### Face mills
#### Fly cutters
#### Roughing vs finishing tools

### Use of collets
### Entering new tools
 * Entering tool details
 * Setting tool offsets

### Training
        
Start with a briefing going through the types of tooling and their uses, with examples of part features created by each tool. A visual reference of tool types, their names and main uses should be available in the CNC area as a reminder.

Next, demonstrate the installation of a tool in a toolholder, including selection and fitting of a suitable collet. The new tool should then be put in the machine, touched-off using a slip block, and entered into the milling software. Have the student repeat the process for a different sized tool.

### Evaluation

The trainee must demonstrate awareness of the most commonly used types of tooling and and when it is appropriate to use each.

The trainee must be able to prepare a new tool for use, including correctly mounting it in a suitable collet and tool holder, entering tool details and setting the tool offset.

## Job planning & toolpath creation

### Job planning considerations
 * Think about machining approach before doing detailed design.
 * Will part fit machine? Think about key dimensions, workholding strategy and tool lengths.
 * What units to use? Metric preferred but inches may be better to fit old/American stuff.
 * How many setups needed? How will each be held and offsetted?
 * What tools required?
 * Once these points are known, detailed design can be done within machine capabilities.

### Basics of modelling and CAM setup in F360
### Use of key operations:
#### 3D adaptive clearing
#### 2D facing
#### 2D contouring
#### Drilling
### Theory and practice of speeds, feeds and depths
### Use of roughing and finishing passes
### Appropriate choice of height settings
### Control of tool operating areas
### Modelling of workholding fixtures
### Use of simulation to detect problems
### Use of machine-specific post processor

### Training

Job planning considerations should be introduced as a briefing with some examples - this might be worth making a presentation for. This is probably best done after the trainee has gone through a basic sample project, but before they start planning more complex jobs.

We will need 3 sample projects written up with corresponding F360 files. Each project will comprise a brief specification for a part and then some guidance on how to prepare the CAD/CAM for that part in F360.

The first project will be very simple and all steps to complete it will be described in detail.

The second project will introduce new features and techniques, and assume that the user can repeat the basic operations introduced in the previous project.

The third project will provide only a specification, and the user will have to accomplish the CAD/CAM themselves.

The instructor should work with the trainee as needed to introduce and demonstrate the software, but the aim should be for the instructions to become sufficient to complete the exercises without extensive help.

For each project, we will have a reference implementation that can be used by the instructor as a reference example, or for the trainee to compare to their solution after completing the exercise.

### Evaluation

The trainee must be able to come up with a viable design and machining plan for a moderately straightforward job. They do not need to get everything right first time, but if they encounter problems they should be able to recognise and solve them independently within a couple of iterations.

The trainee must be generally competent with the main features of the F360 workflow, and able to complete CAD/CAM of a moderately straightforward job themselves.

They should also be able to find and identify problems with a provided F360 project. We should have some projects with some obvious and less-obvious problems to test this, e.g. bad feeds/speeds, toolpaths that will crash, etc.

## Running a CNC job

### Loading programs
### Checklist before run
 * Machine on
 * E-stop released
 * Machine homed
 * Stock securely fastened and squared
 * Work offsets set
 * Tools ready and tool offsets set
 * Loaded tool securely fastened
 * Machine correctly aware of currently loaded tool
 * Machine area clear of debris and loose objects
 * Coolant system running
 * Cover closed
 * Override knobs set appropriately
 * Operator ready on e-stop switch

### Use of start, pause, stop and rewind controls
### Use of block search facility to start mid-program
### Watching for problems
 * Reasonable depth/width of cuts
 * Sensible feed rates
 * Good chip forming
 * No signs of vibration
 * No signs of overheating
 * Tool not obstructed by buildup of chips
 * Program not doing anything unexpected or surprising

### Recovery after emergency stop
* Can work & tool be removed without powering up machine?
* Be aware both may be hot.
* On releasing e-stop, machine will need to home before it can be jogged.
   * Is it safe to do so?
   * May need to home one axis first (generally Z).

### Training

Start with a demonstration of running a job. Then move on to letting the trainee run the job, being ready to prompt & assist them.

A copy of the checklist should be available to the trainee for revision, but the aim should be for them not to need it. A mnemonic acronym for the checklist might be useful if we can come up with one that’s not too long.

We will need to have some jobs prepared with bad parameters. Not too far off to be dangerous, but enough to sound bad or result in a poor finish. We will demonstrate each of these to trainees, then show them how to correct the problem.

Demonstrate use of the emergency stop during a running job. Arrange this such that homing order is important - e.g. with tool down whilst machining a pocket. Show how to bring the machine safely back to a ready state. Have the trainee repeat the exercise for a different scenario.

### Evaluation

The trainee should be able to run a job without prompting or assistance.

The trainee must recognise when a job is failing to satisfy any of the good machining criteria listed above, and use the emergency stop where necessary.

It’s likely that the trainee will encounter some of these problems themselves during their training. If so there will be an opportunity to see if they correct them without prompting.

If such an opportunity doesn’t arise, the trainee can be tested by presenting them with a running job and checking if they can identify and correct a deliberate problem with it.

During one of a trainee’s jobs, press the emergency stop without warning. They must be able to safely bring the machine back to a ready state and continue the job.
