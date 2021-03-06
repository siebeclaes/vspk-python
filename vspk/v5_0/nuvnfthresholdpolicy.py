# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.


from bambou import NURESTObject


class NUVNFThresholdPolicy(NURESTObject):
    """ Represents a VNFThresholdPolicy in the VSD

        Notes:
            Represents thresholds for resources consumed by VNF instance running on NS Gateway and action to be taken when resource utilization crosses configured thresholds.
    """

    __rest_name__ = "vnfthresholdpolicy"
    __resource_name__ = "vnfthresholdpolicies"

    
    ## Constants
    
    CONST_ACTION_SHUTOFF = "SHUTOFF"
    
    CONST_ACTION_NONE = "NONE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a VNFThresholdPolicy instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> vnfthresholdpolicy = NUVNFThresholdPolicy(id=u'xxxx-xxx-xxx-xxx', name=u'VNFThresholdPolicy')
                >>> vnfthresholdpolicy = NUVNFThresholdPolicy(data=my_dict)
        """

        super(NUVNFThresholdPolicy, self).__init__()

        # Read/Write Attributes
        
        self._cpu_threshold = None
        self._name = None
        self._action = None
        self._memory_threshold = None
        self._description = None
        self._min_occurrence = None
        self._monit_interval = None
        self._storage_threshold = None
        
        self.expose_attribute(local_name="cpu_threshold", remote_name="CPUThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="name", remote_name="name", attribute_type=str, is_required=True, is_unique=False)
        self.expose_attribute(local_name="action", remote_name="action", attribute_type=str, is_required=False, is_unique=False, choices=[u'NONE', u'SHUTOFF'])
        self.expose_attribute(local_name="memory_threshold", remote_name="memoryThreshold", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="description", remote_name="description", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="min_occurrence", remote_name="minOccurrence", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="monit_interval", remote_name="monitInterval", attribute_type=int, is_required=False, is_unique=False)
        self.expose_attribute(local_name="storage_threshold", remote_name="storageThreshold", attribute_type=int, is_required=False, is_unique=False)
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def cpu_threshold(self):
        """ Get cpu_threshold value.

            Notes:
                Threshold for CPU usage

                
                This attribute is named `CPUThreshold` in VSD API.
                
        """
        return self._cpu_threshold

    @cpu_threshold.setter
    def cpu_threshold(self, value):
        """ Set cpu_threshold value.

            Notes:
                Threshold for CPU usage

                
                This attribute is named `CPUThreshold` in VSD API.
                
        """
        self._cpu_threshold = value

    
    @property
    def name(self):
        """ Get name value.

            Notes:
                Name of VNF agent policy

                
        """
        return self._name

    @name.setter
    def name(self, value):
        """ Set name value.

            Notes:
                Name of VNF agent policy

                
        """
        self._name = value

    
    @property
    def action(self):
        """ Get action value.

            Notes:
                Action to be taken on threshold crossover

                
        """
        return self._action

    @action.setter
    def action(self, value):
        """ Set action value.

            Notes:
                Action to be taken on threshold crossover

                
        """
        self._action = value

    
    @property
    def memory_threshold(self):
        """ Get memory_threshold value.

            Notes:
                Threshold for memory usage

                
                This attribute is named `memoryThreshold` in VSD API.
                
        """
        return self._memory_threshold

    @memory_threshold.setter
    def memory_threshold(self, value):
        """ Set memory_threshold value.

            Notes:
                Threshold for memory usage

                
                This attribute is named `memoryThreshold` in VSD API.
                
        """
        self._memory_threshold = value

    
    @property
    def description(self):
        """ Get description value.

            Notes:
                Description of VNF agent policy

                
        """
        return self._description

    @description.setter
    def description(self, value):
        """ Set description value.

            Notes:
                Description of VNF agent policy

                
        """
        self._description = value

    
    @property
    def min_occurrence(self):
        """ Get min_occurrence value.

            Notes:
                Minimum number of threshold crossover occurrence during monitoring interval before taking specified action

                
                This attribute is named `minOccurrence` in VSD API.
                
        """
        return self._min_occurrence

    @min_occurrence.setter
    def min_occurrence(self, value):
        """ Set min_occurrence value.

            Notes:
                Minimum number of threshold crossover occurrence during monitoring interval before taking specified action

                
                This attribute is named `minOccurrence` in VSD API.
                
        """
        self._min_occurrence = value

    
    @property
    def monit_interval(self):
        """ Get monit_interval value.

            Notes:
                Monitoring interval (minutes) for threshold crossover occurrences to be considered

                
                This attribute is named `monitInterval` in VSD API.
                
        """
        return self._monit_interval

    @monit_interval.setter
    def monit_interval(self, value):
        """ Set monit_interval value.

            Notes:
                Monitoring interval (minutes) for threshold crossover occurrences to be considered

                
                This attribute is named `monitInterval` in VSD API.
                
        """
        self._monit_interval = value

    
    @property
    def storage_threshold(self):
        """ Get storage_threshold value.

            Notes:
                Threshold for storage usage

                
                This attribute is named `storageThreshold` in VSD API.
                
        """
        return self._storage_threshold

    @storage_threshold.setter
    def storage_threshold(self, value):
        """ Set storage_threshold value.

            Notes:
                Threshold for storage usage

                
                This attribute is named `storageThreshold` in VSD API.
                
        """
        self._storage_threshold = value

    

    