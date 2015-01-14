
import funtool.state_measure
import numbers

def all_ratios(state_measure, analysis_collection, state_collection, overriding_parameters=None):
    measure_parameters = funtool.state_measure.get_measure_parameters(state_measure, overriding_parameters)
    all_measures= list(analysis_collection.state.measures.keys())
    for idx,first_measure in enumerate(all_measures):
        if isinstance(analysis_collection.state.measures[first_measure],numbers.Number):
            for second_measure in all_measures[(idx+1):-1]:
                if isinstance(analysis_collection.state.measures[second_measure],numbers.Number):
                    a_value= analysis_collection.state.measures[first_measure]
                    b_value= analysis_collection.state.measures[second_measure]
                    analysis_collection.state.measures[first_measure+"_to_"+second_measure]= funtool.state_measures.default._compute_ratio(a_value,b_value)
    return analysis_collection

@funtool.state_measure.state_and_parameter_measure
def number_of_scripts(state,parameters):
    return len(state_scripts(state))

#duplicate of function in funtool_scratch_processes.state_measures.default
def state_scripts(state):   
    json_data= state.data.get('json')
    scripts=[]
    if json_data != None:
        scripts.extend(json_data.get('scripts',[]))
        for child in json_data.get('children'):
            scripts.extend(child.get('scripts',[]))
    return scripts
    
    
    #1. Counting number of Sprites
@funtool.state_measure.state_and_parameter_measure
def number_of_sprites(state,parameters)
	json_data = state.data.get('json')
	sprites=[]
    	if json_data != None:
     	   sprites.extend(json_data.get('info',[]))
  	return sprites.spriteCount


#2(a). Counting number of Scripts 
@funtool.state_measure.state_and_parameter_measure
def number_of_scripts(state,parameters)
	json_data = state.data.get('json')
	scripts=[]
    	if json_data != None:
     	   scripts.extend(json_data.get('info',[]))
  	return scripts.scriptCount

#2(b). Counting number of Scripts 
@funtool.state_measure.state_and_parameter_measure
def number_of_scripts(state,parameters)
	json_data = state.data.get('json')
	scripts=[]
	count=0
    	if json_data != None:
     	   for script in json_data.get('scripts'):
		count=count+1
  	return count


#3. Getting out all info for that state
@funtool.state_measure.state_and_parameter_measure
def state_info(state,parameters)
	json_data = state.data.get('json')
	info=[]
    	if json_data != None:
     	   info.extend(json_data.get('info',[]))
  	return info


#4. Counting number of states having costumes with hats
@funtool.state_measure.state_and_parameter_measure
def number_of_scripts_with_hats(state,parameters)
	json_data = state.data.get('json')
	costumes=[]
	count=0
    	if json_data != None:
     	   costumes.extend(json_data.get('costumes',[]))
	   if costumes.costumeName == 'costume 1' or costumes.costumeName == 'costume 2' or costumes.costumeName == 'costume 3':
		count=count+1
  	return count
